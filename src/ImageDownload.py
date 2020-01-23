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
    root.geometry("400x300")

    # ラベル
    Static1 = tkinter.Label(text="ImageDownload")
    Static1.pack()

    #エントリー
    EditBox = tkinter.Entry()
    EditBox.insert(tkinter.END,"女優名を入力してね")
    EditBox.pack()

    #ここで，valueにEntryの中身が入る
    value = EditBox.get()
    actless = value
    root.mainloop()

def main():
    GUI()

if __name__ == "__main__":
    main()