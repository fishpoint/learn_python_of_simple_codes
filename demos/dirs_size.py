# -*- coding: utf-8 -*-
__author__ = "YuDian"
def get_files(dir):
    AllSize=0
    for(root,dirs,files) in os.walk(dir):
        for file in files:
            AllSize=AllSize+single_size(os.path.join(root,file))
    return int(AllSize/1024/1024)

def single_size(FileName):
    # BeautifulSize=size_change(os.path.getsize(FileName))
    return os.path.getsize(FileName)/1024

def size_change(size):
    size=size/1024     #Kb
    if(size>=1024):
        size=size/1024   # Mb
        if(size>1024):
            size=size/1024
    return int(size)

import os
dir=r'F:\for_python'
if os.path.exists(dir):
    if os.path.isdir(dir):
        print(get_files(dir))
    else:
        print('Error -> Please Enter a dir')
else:
    print('no find'+dir)