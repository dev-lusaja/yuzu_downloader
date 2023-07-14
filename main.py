from src.yuzu import Yuzu
from src.zip_downloader import YuzuWinDownloader
from dotenv import load_dotenv

load_dotenv()
yuzu_downloader = YuzuWinDownloader(
    yuzu=Yuzu()
)

yuzu_downloader.download()
