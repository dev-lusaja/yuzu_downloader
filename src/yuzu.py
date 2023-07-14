import requests


class Yuzu:

    def __init__(self):
        self.__latest_release = "https://api.github.com/repos/yuzu-emu/yuzu-mainline/releases/latest"
        self.__zip_file = None
        self.__release_name = None

    def latest_release(self):
        res = requests.get(self.__latest_release)
        body = res.json()
        for asset in body['assets']:
            download_url = asset['browser_download_url']
            if download_url[-4:] == '.zip':
                self.__zip_file = asset['browser_download_url']

        if self.__zip_file is None:
            raise Exception('No zip file')

        self.__release_name = body['name']

        return self.__zip_file

    @staticmethod
    def unzip_name():
        return 'yuzu-windows-msvc'

    def release_name(self):
        return self.__release_name
