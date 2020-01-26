# coding: utf-8

import numpy as np
import pickle
from sklearn.model_selection import train_test_split

class Dataset():
    def __init__(self, X=None, y=None, path = None):
        """
        機械学習データセット
        Arguments:
            X: 説明変数
            y: 目的変数
            path: ファイルパス
        """
        self.X = X
        self.y = y
        self.path = path

    def read_pickle(self, input_path):
        """
        pickle形式のデータセットを読み込む
        Arguments:
            input_path: pickleが保存されているパスを指定
        """
        with open(input_path, mode="rb") as f:
            tmp = pickle.load(f)
        self.X = tmp.X
        self.y = tmp.y
        self.path = tmp.path

    def set_data(self, X, y, path=None):
        """
        機械学習データセットを設定する
        Arguments:
            X: 説明変数(numpy配列)
            y: 目的変数(numpy配列)
        """
        self.X = X
        self.y = y
        self.path = path

    def split_data(self, ratio=0.2):
        """
        学習データとテストデータに分ける
        Arguments:
            ratio: テストデータの割合
        """
        self.X_train, self.X_test, self.y_train, self.y_test, self.path_train, self.path_test = train_test_split(self.X, self.y, self.path, test_size=ratio)

    def to_pickle(self, output_path):
        """
        データセットをpickle形式で保存する
        Arguments:
            output_path: pickleを保存するパスを指定
        """
        with open(output_path, mode="wb") as f:
            pickle.dump(self, f)