import os
import nibabel as nib
import pandas as pd
import numpy as np
from nibabel import four_to_three
import SimpleITK as sitk
from diagnosis.src.Utils.configuration_parser import ResourcesConfiguration


def adjust_input_volume_for_nifti(volume_path, output_folder):
    if not os.path.isdir(volume_path):
        output_path = volume_path
        buff = os.path.basename(volume_path).split('.')
        extension = ''
        if len(buff) == 2:
            extension = buff[-1]
        elif len(buff) > 2:
            extension = buff[-2] + '.' + buff[-1]

        if extension != 'nii.gz' or extension != 'nii':
            image_sitk = sitk.ReadImage(volume_path)
            output_path = os.path.join(output_folder, 'tmp',
                                       os.path.basename(volume_path).split('.')[0] + '.nii.gz')
            os.makedirs(os.path.dirname(output_path))
            sitk.WriteImage(image_sitk, output_path)
    else:  # DICOM folder case
        reader = sitk.ImageSeriesReader()
        dicom_names = reader.GetGDCMSeriesFileNames(volume_path)
        reader.SetFileNames(dicom_names)
        image = reader.Execute()
        output_path = os.path.join(output_folder, 'tmp', 'converted_input.nii.gz')
        os.makedirs(os.path.dirname(output_path))
        sitk.WriteImage(image, output_path)

    return output_path


def load_nifti_volume(volume_path):
    nib_volume = nib.load(volume_path)
    if len(nib_volume.shape) > 3:
        if len(nib_volume.shape) == 4:  # Common problem
            nib_volume = four_to_three(nib_volume)[0]
        else:  # DWI volumes
            nib_volume = nib.Nifti1Image(nib_volume.get_data()[:, :, :, 0, 0], affine=nib_volume.affine)

    return nib_volume


def dump_predictions(predictions, parameters, nib_volume, storage_prefix):
    print("Writing predictions to files...")
    naming_suffix = 'pred' if parameters.predictions_reconstruction_method == 'probabilities' else 'labels'
    class_names = parameters.training_class_names

    if len(predictions.shape) == 4:
        for c in range(1, predictions.shape[-1]):
            img = nib.Nifti1Image(predictions[..., c], affine=nib_volume.affine)
            predictions_output_path = os.path.join(storage_prefix + '-' + naming_suffix + '_' + class_names[c] + '.nii.gz')
            os.makedirs(os.path.dirname(predictions_output_path), exist_ok=True)
            nib.save(img, predictions_output_path)
    else:
        img = nib.Nifti1Image(predictions, affine=nib_volume.affine)
        predictions_output_path = os.path.join(storage_prefix + '-' + naming_suffix + '_' + 'argmax' + '.nii.gz')
        os.makedirs(os.path.dirname(predictions_output_path), exist_ok=True)
        nib.save(img, predictions_output_path)
