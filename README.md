# Glioblastoma Surgery Imaging - Reporting And Data System (GSI-RADS)

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)
[![GitHub Downloads](https://img.shields.io/github/downloads/SINTEFMedtek/GSI-RADS/total?label=GitHub%20downloads&logo=github)](https://github.com/SINTEFMedtek/GSI-RADS/releases)

![GUI](GIS-RADS_illustration.png)

## 1. Description
The repository contains the software to automatically compute glioblastoma's features from a T1-wighted MRI pre-operative MRI,
and report them in a standardized manner, as originally introduced in the article below-mentionned.

Please cite the following article if you have used our software in one of your studies:
>`@article{,`  
      `title={Glioblastoma Surgery Imaging - Reporting and Data System: standardized reporting of tumor volume, location, and resectability based on automated segmentations},`  
      `author={},`  
      `year={2021},`  
      `journal={Cancers},`  
`}`

## 2. Softwares and usage
An executable is provided for the three main Operating Systems: Windows 10 (64-bit), macOS (>= high sierra), and Ubuntu Linux 18.04.
The software can be downloaded from [here](https://github.com/SINTEFMedtek/GSI-RADS/releases) (see under **Assets**). 

### 2.1 Download and installation  
These steps are only needed to do once:
1) Download the executable to your Operating System.  
2) On macOS/Ubuntu only: Open terminal, write `chmod +x `, drag and drop the file into the terminal window, and click Enter, to enable running program as executable.
3) Right-click and open to execute the file named GSI-RADS.

Then for all future use, simply double-click to launch the software.

**GSI-RADS might take up to a minute to start.** This is because the software has to be unpackaged at runtime. Some operating systems run an anti-virus check when unpackaging content. On Windows this is called **real-time protection**. This further slows down the unpackaging process. We will look into how to solve this issue in the near future.  
The software may appear unresponsive when running analysis.

### 2.2 Usage  
  1) Click 'Input MRI...' to select from your file explorer the MRI scan to process (unique file).  
  1*) Alternatively, Click 'File > Import DICOM...' if you wish to process an MRI scan as a DICOM sequence.  
  2) Click 'Output destination' to choose a directory where to save the results.  
  3) (OPTIONAL) Click 'Input segmentation' to choose a tumor segmentation mask file, if nothing is provided the internal model with generate the segmentation automatically.  
  4) Click 'Run diagnosis' to perform the analysis. The human-readable version of the results will be displayed directly in the interface.  
  
  NOTE: The output folder is populated automatically with the following:  
       * The diagnosis results in human-readable text (report.txt) and Excel-ready format (report.csv).  
       * The automatic segmentation masks of the brain and the tumor in the original patient space (input_brain_mask.nii.gz and input_tumor_mask.nii.gz).  
       * The anatomical structures mask in original patient space (input_anatomical_regions_mask.nii.gz).  
       * The input volume and tumor segmentation mask in MNI space in the sub-directory named \'registration\'.  

## 3. Computed features  
The following features are automatically computed and reported to the user:
- **Multifocality**: whether the tumor is multifocal or not, the total number of foci, and the largest minimum distance between two foci.  
- **Volume**: total tumor volume in original patient space and MNI space (in ml).  
- **Laterality**: tumor percentage in each hemisphere, and assessment of midline crossing.  
- **Resectability**: expected resectbale and residual volumes (in ml), and resection index.  
- **Subcortical structures**: percentage of the tumor volume overlapping each structure from the MNI atlas, the Hard-Oxford atlas, and Schaefer atlas.  
- **White matter tracts**: percentage of the tumor volume overlapping each tract from the BrainLab atlas. If no overlap, the minimum distance to the tract is provided (in mm).  
