import sys
import matplotlib.pyplot as plt
import cv2
import os
import re
import pdb
from face_detectors.dlib_face_detector import detect_face as dlib_df
from face_detectors.haar_face_detector import detect_face as haar_df
from tqdm import trange, tqdm

image_ext = re.compile(r'\.jpg|\.jpg')

def main():
    path = sys.argv[1]
    fast = true if len(sys.argv) > 2 else false
    if os.path.isdir(path):
        for filepath in tqdm(os.listdir(path)):
            extension = os.path.splitext(filepath)[1]
            if image_ext.match(extension):
                detect_face(path + '/' + filepath, fast)
    elif os.path.isfile(path):
        detect_face(path, fast)
    else:
        os.exit(1)

def detect_face(imagepath, fast=True):
    if fast:
        haar_df(imagepath)
    else:
        dlib_df(imagepath)

if __name__ == "__main__":
    main()
