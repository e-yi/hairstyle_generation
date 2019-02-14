import os
import cv2
import sys
import argparse
import numpy as np
from PIL import Image

def dfsFile(path,func):
    """
    给定根目录，dfs寻找其下所有文件进行统一操作
    """
    for file in os.listdir(path):
        fullPath = os.path.join(path,file)
        if os.path.isdir(fullPath):
            dfsFile(fullPath,func)
        else:
            func(file,fullPath)

def resize(im):
    new_width = new_height = 256
    width, height = im.size   # Get dimensions
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    return im.crop((left, top, right, bottom))

def edge(im,output_dir,k=(11,11),lb=50,ub=90):
    img = np.array(im)
    gaussian = cv2.GaussianBlur(src=img, ksize=k, sigmaX=0, sigmaY=0)
    canny = cv2.Canny(gaussian, lb, ub)
    cv2.imwrite(output_dir,canny) # save img
    
def process(file,output_resize,output_canny,output_concat):
    im = Image.open(file)
    im = resize(im)
    im.save(output_resize)
    edge(im,output_canny)
    
    list_im = [output_resize, output_canny]
    imgs    = [ Image.open(i).convert('RGB') for i in list_im ]
    assert imgs[0].size == imgs[1].size
    imgs_comb = np.hstack( (np.asarray(i) for i in imgs ) )
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save(output_concat)
    
def batchProcess(input_dir, output_dir):
    output_resize = os.path.join(output_dir,'resize')
    output_canny = os.path.join(output_dir,'canny')
    output_concat = os.path.join(output_dir,'concat')
    os.makedirs(output_resize,exist_ok=True)
    os.makedirs(output_canny,exist_ok=True)
    os.makedirs(output_concat,exist_ok=True)
    def f(file,fullPath):
        r = os.path.join(output_resize,file)
        ca = os.path.join(output_canny,file)
        co = os.path.join(output_concat,file)
        return process(fullPath,r,ca,co)
    dfsFile(input_dir, f)


parser = argparse.ArgumentParser(
formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--dataroot', help='path to images')
parser.add_argument('--output_dir', help='path to store processed images')
args = parser.parse_args()
batchProcess(args.dataroot,args.output_dir)
