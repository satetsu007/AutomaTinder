import cv2
import os
import warnings
warnings.filterwarnings('ignore')

def face_detect():
    #サイズ指定
    height = 100
    width = 100
    ratio = 0.25

    face_cascade_path = './models/xml/haarcascade_frontalface_default.xml'
    eye_cascade_path = './models/xml/haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    category_path = "./data/org"

    for category in [category for category in os.listdir(category_path) if category!=".DS_Store"]:
        folder_path = "{}/{}".format(category_path, category)
        to_folder_path = folder_path.replace("org", "detect")
        if not os.path.isdir(to_folder_path):
            os.mkdir(to_folder_path)
        for folder in [folder for folder in os.listdir(folder_path) if folder!=".DS_Store"]:
            name_path = "{}/{}".format(folder_path, folder)
            to_name_path = name_path.replace("org", "detect")
            if not os.path.isdir(to_name_path):
                os.mkdir(to_name_path)
            for name in [name for name in os.listdir(name_path) if name!=".DS_Store"]:
                img_path = "{}/{}".format(name_path, name)
                to_img_path = img_path.replace("org", "detect")
                img = cv2.imread(img_path)
                try:
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                except:
                    continue
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    try:
                        detect_img = img[int(y-h*ratio):int(y+h*(1+ratio)), int(x-w*ratio):int(x+w*(1+ratio)), :]
                        dst = cv2.resize(detect_img, dsize=(height, width))
                        cv2.imwrite(to_img_path, dst)
                    except:
                        continue

def main():
    face_detect()

if __name__ == "__main__":
    main()