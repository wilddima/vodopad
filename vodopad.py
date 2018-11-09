import sys
import matplotlib.pyplot as plt
import cv2
import os
import re
import pdb
import face_recognition
from face_detectors.dlib_face_detector import detect_face as dlib_df
from face_detectors.haar_face_detector import detect_face as haar_df
from tqdm import trange, tqdm

image_ext = re.compile(r'\.jpg|\.JPG')

def main():
    path = sys.argv[1]
    fast = sys.argv[2]
    if os.path.isdir(path):
        for filepath in tqdm(os.listdir(path)):
            extension = os.path.splitext(filepath)[1]
            if image_ext.match(extension):
                if fast:
                    haar_df(path + '/' + filepath)
                else:
                    dlib_df(path + '/' + filepath)
    elif os.path.isfile(path):
        determine_face(path)
    else:
        os.exit(1)

def determine_face(imagepath):
    image = face_recognition.load_image_file(imagepath)
    faces = face_recognition.face_locations(image)
    for (top, right, bottom, left) in faces:
        cv2.rectangle(image, (left, top), (right, bottom), (255,0,0),2)

    plt.rcParams['figure.figsize'] = 18,10
    plt.imshow(image)
    plt.title('Image', fontsize=15)
    plt.axis('off')
    plt.show()

def haarcascade_determine_face(imagepath):
    face_cascade = cv2.CascadeClassifier('vendor/haarcascade_frontalface_default.xml')
    image = cv2.imread(imagepath)
    gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    plt.rcParams['figure.figsize'] = 18,10
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Image', fontsize=15)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
