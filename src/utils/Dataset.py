# coding: utf-8

import numpy as np
import pickle
from sklearn.model_selection import train_test_split

class Dataset():
    def __init__(self, X=None, y=None):
        """
        機械学習データセット
        Arguments:
            X {[type]} -- [description]
            y {[type]} -- [description]
        """
        self.X = X
        self.y = y

    def read_pickle(self, input_path):
        """
        pickle形式のデータセットを読み込む
        Arguments:
            input_path {[type]} -- [description]
        """
        with open(input_path, mode="rb") as f:
            self = pickle.load(input_path)

    def set_data(self, X, y):
        """
        機械学習データセットを設定する
        Arguments:
            X: 説明変数(numpy配列)
            y: 目的変数(numpy配列)
        """
        self.X = X
        self.y = y

    def split_data(self, ratio):
        """
        学習データとテストデータに分ける
        Arguments:
            ratio: テストデータの割合
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y)

    def to_pickle(self, output_path):
        """
        データセットをpickle形式で保存する
        Arguments:
            output_path: 保存するパス・ファイル名を指定
        """
        with open(output_path, mode="wb") as f:
            pickle.dump(self, f)