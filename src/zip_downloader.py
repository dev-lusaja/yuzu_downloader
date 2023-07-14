import os
import shutil
import requests
from zipfile import ZipFile
from src.yuzu import Yuzu
from clint.textui import progress


class YuzuWinDownloader:

    def __init__(self, yuzu: Yuzu):
        self.yuzu = yuzu
        self.__url = self.yuzu.latest_release()
        self.__dest_path = os.getenv('DOWNLOAD_FOLDER')
        self.__current_dir = os.path.dirname(self.__dest_path)
        self.__name = 'yuzu_download.zip'
        self.__zip_path = os.path.join(self.__current_dir, self.__name)
        self.__unzip_path = os.path.join(self.__current_dir, self.yuzu.unzip_name())

    def download(self):
        response = requests.get(self.__url, stream=True)
        print('Downloading...')
        with open(self.__zip_path, "wb") as file:
            total_length = int(response.headers.get('content-length'))
            for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1):
                file.write(chunk)
        self.unzip()
        self.remove_zip()
        self.copy()
        self.remove_unzip()

    def unzip(self):
        with ZipFile(self.__zip_path, 'r') as zObject:
            zObject.extractall(self.__current_dir)

    def remove_zip(self):
        os.remove(self.__zip_path)

    def remove_unzip(self):
        shutil.rmtree(self.__unzip_path)

    def copy(self):
        shutil.copytree(src=self.__unzip_path, dst=self.__dest_path, dirs_exist_ok=True)
        print('Successful Yuzu download (%s)!!!' % self.yuzu.release_name())
        print('Yuzu was downloaded on %s directory' % self.__dest_path)
