import sys
import matplotlib.pyplot as plt
import cv2
import os
import re
import pdb
from face_detectors.dlib_face_detector import detect_face as dlib_df
from face_detectors.haar_face_detector import detect_face as haar_df
from face_identifiers.dlib_face_identifier import identify_face as dlib_if
from face_identifiers.dlib_face_identifier import identify_face as dlib_if
from face_identifiers.dlib_face_identifier import DlibFaceIdentifier, image_ext
from tqdm import trange, tqdm

def main():
    path = sys.argv[1]
    reference = sys.argv[2]
    face_ident = DlibFaceIdentifier(reference, True)
    if os.path.isdir(path):
        for filepath in tqdm(os.listdir(path)):
            extension = os.path.splitext(filepath)[1]
            if image_ext.match(extension):
                face_ident.identify(path + '/' + filepath)
    elif os.path.isfile(path):
        face_ident.identify(path)
    else:
        sys.exit(1)

def identify_face(imagepath, reference, ident):
    dlib_if(imagepath, reference)

if __name__ == "__main__":
    main()
