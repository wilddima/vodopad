import sys
import matplotlib.pyplot as plt
import cv2
import os
import re
import pdb
from .dlib_face_identifier import DlibFaceIdentifier, image_ext
from tqdm import trange, tqdm
import click
from shutil import copy

@click.command()
@click.argument('path')
@click.option('--people', '-p', help='Photo or path to the folder with photos of people that will be used as samples for clustering')
@click.option('--move/--no-move', default=False, help='Moving photo to folders instead of copying')
@click.option('--output', '-o', default='./', help='Path to folder for storing clustered photos')
def main(path, people, move, output):
    """Simple toolkit for automation searching and clustering photos based on people

    Usage

    Argument is an image or folder of images for clustering.
    Created folders will be named as people photos.

    vodopad ./photos_folder ./me.jpg
    """
    face_ident = DlibFaceIdentifier(people, False)
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

    if move:
        print('Moving ...')
    else:
        print('Copying ...')

    for result in tqdm(results):
        img_path, exists = result
        for name, isexist in zip(exists.keys(), exists.values()):
            if isexist:
                dir_path = os.path.join(output, name)
                if not os.path.isdir(dir_path):
                    os.makedirs(dir_path)
                copy(img_path, dir_path)
        if True in exists.values() and move:
            os.remove(img_path)
