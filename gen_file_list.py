#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import os
import glob

def gen_file_list(bpath, train=True):
    if train:
        Subject = 'S'
        mid_path = 'imageFrames/video_[0-9]*'
        fname_re = 'frame_[0-9]*.jpg'
        ofname = 'train.txt'
    else:
        Subject = 'TS'
        mid_path = 'imageSequence'
        fname_re = 'img_[0-9]*.jpg'
        ofname = 'test.txt'

    with open(os.path.join(bpath, ofname), 'w') as f:
        fpath = os.path.join(bpath, '{}[0-9]*'.format(Subject), 'Seq*', mid_path, fname_re)
        fnames = glob.glob(fpath)
        fnames = list(map(lambda x: x+'\n', fnames))
        f.writelines(fnames)

if __name__ == '__main__':
    with open('./conf.ig') as f:
    context = f.read()
    ready_to_download = re.search(r'ready_to_download=.', context).group()[-1]
    assert ready_to_download != '0', 'Please read the documentation and edit the config file accordingly.'
    destination = re.split(r'\'', re.search(r'destination=[a-zA-Z0-9_./\'"]+', context).group())[1]
    subjects = re.split(r' ', re.sub(r'\( | \)|\(|\)', '',
                        re.search(r'subjects=\([0-9 ]+\)', context).group()[9:]))
    print('generate a list file containing available frames with their paths in ' + destination)
    gen_file_list(bpath=destination, train=True)