import cv2
import os
import warnings
from tqdm import tqdm
warnings.filterwarnings('ignore')

def face_detect(height, width, ratio):

    face_cascade_path = './models/xml/haarcascade_frontalface_default.xml'
    eye_cascade_path = './models/xml/haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    category_path = "./data/org"

    for category in tqdm([category for category in os.listdir(category_path) if category!=".DS_Store"], desc="category", leave=False):
        folder_path = "{}/{}".format(category_path, category)
        to_folder_path = folder_path.replace("org", "detect")
        if not os.path.isdir(to_folder_path):
            os.mkdir(to_folder_path)
        for folder in tqdm([folder for folder in os.listdir(folder_path) if folder!=".DS_Store"], desc=category, leave=False):
            name_path = "{}/{}".format(folder_path, folder)
            to_name_path = name_path.replace("org", "detect")
            if not os.path.isdir(to_name_path):
                os.mkdir(to_name_path)
            for name in tqdm([name for name in os.listdir(name_path) if name!=".DS_Store"], desc=folder, leave=False):
                img_path = "{}/{}".format(name_path, name)
                #to_img_path = "{}/{}_{}".format(name_path, i, name).replace("org", "detect")
                img = cv2.imread(img_path)
                try:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                except:
                    continue
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for i, (x,y,w,h) in tqdm(enumerate(faces), desc="face", leave=False):
                    to_img_path = "{}/{}_{}".format(name_path, i, name).replace("org", "detect")
                    detect_img = FaceCrop(img, ratio, x, y, w, h)
                    dst = cv2.resize(detect_img, dsize=(height, width))
                    cv2.imwrite(to_img_path, dst)

def FaceCrop(img, ratio, x, y, w, h):
    """検出した顔を画像の中から切り出す

    Arguments:
        img: 元画像
        ratio: 切り出した画像を拡大する割合
        x: 検出した顔の左上点のx座標
        y: 検出した顔の左上点のx座標
        w: 検出した顔の横幅
        h: 検出した顔の縦幅
    """
    x1 = int(x - w * ratio)
    x2 = int(x + w * (1 + ratio))
    y1 = int(y - h * ratio)
    y2 = int(y + h * (1 + ratio))
    # 画像の左端を超える場合
    if x1 < 0:
        x1 = 0
    # 画像の右端を越える場合
    if x2 > img.shape[1]:
        x2 = img.shape[1]
    # 画像の上端を超える場合
    if y1 < 0:
        y1 = 0
    # 画像の下端を越える場合
    if y2 > img.shape[0]:
        y2 = img.shape[0]

    # 画像を切り出す
    crop_img = img[y1:y2, x1:x2, :]

    return crop_img

def main():
    # 出力画像のサイズ指定
    height = 100
    width = 100
    # 検出した範囲の拡大率
    ratio = 0.25
    face_detect(height, width, ratio)

if __name__ == "__main__":
    main()