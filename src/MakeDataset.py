import os
import numpy as np
import pandas as pd
import sys
import random
from tqdm import tqdm
import cv2

sys.path.append("./src/utils")
sys.path.append("./src")

from Dataset import Dataset

def MakeDataset(pickle_path, category_path, like_list, dislike_list):
    """
    """
    img_list = []
    label_list = []
    path_list = []
    for category in [category for category in os.listdir(category_path) if category!=".DS_Store"]:
        folder_path = "{}/{}".format(category_path, category)
        for folder in [folder for folder in os.listdir(folder_path) if folder!=".DS_Store"]:
            name_path = "{}/{}".format(folder_path, folder)
            for name in [name for name in os.listdir(name_path) if name!=".DS_Store"]:
                img_path = "{}/{}".format(name_path, name)
                # 画像を読み込む
                img = cv2.imread(img_path)
                img_list.append(img)
                path_list.append(img_path)
                # 教師ラベルを付与
                if folder in like_list:
                    label_list.append(1)
                elif folder in dislike_list:
                    label_list.append(0)

    img_array = np.array(img_list)
    label_array = np.array(label_list)
    path_array = np.array(path_list)

    dataset = Dataset()
    dataset.set_data(img_array, label_array, path_array)
    print("データセットを", pickle_path, end="")
    print("に保存します")
    dataset.to_pickle(pickle_path)

def main():
    pickle_path = "./data/dataset.pkl"
    category_path = "./data/annotation"

    name_list = []

    for category in [category for category in os.listdir(category_path) if category!=".DS_Store"]:
        folder_path = "{}/{}".format(category_path, category)
        for folder in [folder for folder in os.listdir(folder_path) if folder!=".DS_Store"]:
            name_list.append(folder)

    # 好みの女性リスト
    like_list = ["篠田麻里子", "前田敦子",
                "波瑠", "永野芽郁", "新木優子",
                "浜辺美波", "吉岡里帆", "杉咲花",
                "堀北真希", "栗山千明", "清野菜名",
                "本田翼", "小松菜奈", "有村架純",
                "広瀬すず", "松岡茉優", "中条あやみ"]

    dislike_list = [name for name in name_list if not name in like_list]

    # 女性リスト
    print("-" * 50)
    print("好みの女性")
    for i, name in enumerate(like_list):
        if (i+1) % 5==0:
            print(name)
        else:
            print(name, end="\t")

    print("")
    print("-" * 50)
    print("好みでない女性")
    for i, name in enumerate(dislike_list):
        if (i+1) % 5==0:
            print(name)
        else:
            print(name, end="\t")

    print("")
    print("")
    print("-" * 50)
    print("データセットを作成します")
    MakeDataset(pickle_path, category_path, like_list, dislike_list)
    print("データセットを作成しました")
    print("終了します...")

if __name__ == "__main__":
    main()