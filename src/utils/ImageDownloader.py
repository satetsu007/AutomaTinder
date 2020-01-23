import os
from google_images_download import google_images_download

class ImageDownloader:
    def __init__(self, keyword, numImages):
        """
        keyword: 検索ワード
        numImages: 上限数
        """
        self._set_keyword(keyword)
        self._set_numImages(numImages)
        self.downloader = google_images_download.googleimagesdownload()

    def download(self, output_directory):
        """
        output_directory: 相対パス
        """
        print("start downloading.")
        arg = {"keywords": self.keyword, "limit": self.numImages, "no_numbering": True,
               "print_urls": False, "output_directory": output_directory}
        paths = self.downloader.download(arg)
        print("finish downloading.")

    def _set_keyword(self, keyword):
        self.keyword = keyword

    def _set_numImages(self, numImages):
        self.numImages = numImages