# coding: utf-8

import os
import numpy as np
import pandas as pd
from google_images_download import google_images_download
import sys
import matplotlib.pyplot as plt
import random

sys.path.append("./src")
sys.path.append("./src/utils")

from ImageDownloader import ImageDownloader
import tkinter

def GUI():
    root = tkinter.Tk()
    root.title("ImageDownloader")
    root.mainloop()
    # 女優名を格納する
    actless = [""]

def main():
    GUI()

if __name__ == "__main__":
    main()