import sys
import cv2
import os
import re
import pdb
from .dlib_face_identifier import DlibFaceIdentifier, image_ext
from tqdm import trange, tqdm
import click
from shutil import copy
from emoji import emojize

@click.command()
@click.argument('path', nargs=-1)
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
    output = os.path.expanduser(output)

    img_pathes = find_images(path)

    print(emojize('Found {} images :camera:'.format(len(img_pathes)), use_aliases=True))

    if len(img_pathes) == 0: sys.exit(0)

    if move:
        print('Recognition and moving ...')
    else:
        print('Recognition and copying ...')

    transered_count = 0

    for pth in tqdm(img_pathes):
        if transfer_image(face_ident.identify(pth), output, move): transered_count += 1

    print('Copied {} photos to {}'.format(transered_count, output))

def transfer_image(result, output, move):
    img_path, exists = result
    transfered = False
    for name, isexist in zip(exists.keys(), exists.values()):
        if isexist:
            dir_path = os.path.join(output, name)
            if not os.path.isdir(dir_path):
                os.makedirs(dir_path)
            copy(img_path, dir_path)
            transfered = True
    if True in exists.values() and move:
        os.remove(img_path)
    return transfered

def find_images(path):
    img_pathes = []
    for pth in path:
        if os.path.isdir(pth):
            for filepath in os.listdir(pth):
                img_path = full_image_path(os.path.join(pth, filepath))
                if img_path: img_pathes.append(img_path)
        elif os.path.isfile(pth):
            img_path = full_image_path(pth)
            if img_path: img_pathes.append(img_path)
    return img_pathes

def full_image_path(path):
    extension = os.path.splitext(path)[1]
    if image_ext.match(extension):
        return os.path.expanduser(path)
