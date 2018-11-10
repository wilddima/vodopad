import sys
import matplotlib.pyplot as plt
import cv2
import os
import re
import pdb
from face_identifiers.dlib_face_identifier import DlibFaceIdentifier, image_ext
from tqdm import trange, tqdm

def main():
    path = sys.argv[1]
    reference = sys.argv[2]
    face_ident = DlibFaceIdentifier(reference, False)
    results = []

    print('Recognition ...')
    if os.path.isdir(path):
        for filepath in tqdm(os.listdir(path)):
            extension = os.path.splitext(filepath)[1]
            if image_ext.match(extension):
               results.append(face_ident.identify(path + '/' + filepath))
    elif os.path.isfile(path):
        results.append(face_ident.identify(path))
    else:
        sys.exit(1)

    print('Copying ...')
    for result in tqdm(results):
        img_path, exists = result
        for name, isexist in zip(exists.keys(), exists.values()):
            if isexist:
                if not os.path.isdir(name):
                    os.mkdir(name)
                os.system("cp {} {}".format(img_path, name))

if __name__ == "__main__":
    main()
