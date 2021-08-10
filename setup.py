import os
import gdown


def setup_repository():
    # Downloading, extracting models.
    models_url = 'https://drive.google.com/uc?id=1ga08d8QQfAHOgTSKiPpIN7f_owuicNUA'
    models_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources', 'models')
    os.makedirs(models_path, exist_ok=True)
    md5 = '55c66e000de9077e483635029f740901'
    models_archive_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'models.zip')
    gdown.cached_download(url=models_url, path=models_archive_path, md5=md5)
    gdown.extractall(path=models_archive_path, to=models_path)
    os.remove(models_archive_path)


setup_repository()
