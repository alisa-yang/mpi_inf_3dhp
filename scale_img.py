#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# This script uses conf.ig as the configuration file

import re
import os
import cv2
from multiprocessing.dummy import Pool as ThreadPool


dest_size = 368  # the desired frame size

def scale_img(frame):
    print('scaling frame {} in {}'.format(frame, img_dir))
    img_path = os.path.join(img_dir, frame)
    img = cv2.imread(img_path)
    img = cv2.resize(img, (dest_size, dest_size))
    cv2.imwrite(img_path, img)

with open('./conf.ig') as f:
    context = f.read()
    ready_to_download = re.search(r'ready_to_download=.', context).group()[-1]
    assert ready_to_download != '0', 'Please read the documentation and edit the config file accordingly.'
    destination = re.split(r'\'', re.search(r'destination=.*\n', context).group())[1]
    destination = os.getcwd() if destination=='./' else destination
    subjects = re.split(r' ', re.sub(r'\( | \)|\(|\)', '',
                        re.search(r'subjects=\([0-9 ]+\)', context).group()[9:]))
print('scale frame images in ' + destination)
for sbj in subjects:
    for seq in [1, 2]:
        cam_dir_root = os.path.join(destination, 'S{}'.format(sbj), 'Seq{}'.format(seq), 'imageFrames')
        for cam in os.listdir(cam_dir_root):
            img_dir = os.path.join(cam_dir_root, cam)
            print('\n...{}...'.format(img_dir))
            frames = os.listdir(img_dir)
            pool = ThreadPool(os.cpu_count())
            pool.map(scale_img, frames)
            pool.close()
            pool.join()
print('done.')
