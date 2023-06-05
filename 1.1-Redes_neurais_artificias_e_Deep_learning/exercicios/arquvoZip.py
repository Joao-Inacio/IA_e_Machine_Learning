import os
import shutil
import zipfile


def descompactar(zip_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

        # Descompactando o arquivo zip
        zip_object = zipfile.ZipFile(file=zip_path, mode='r')
        zip_object.extractall(path=dest_path)
        zip_object.close()
    else:
        zip_object = zipfile.ZipFile(file=zip_path, mode='r')
        zip_object.extractall(path=dest_path)
        zip_object.close()
