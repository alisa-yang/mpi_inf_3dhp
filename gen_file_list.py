#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

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
    gen_file_list(bpath='./', train=True)