#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

def compute_historgram(img):
    hstg = {}
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            c = hstg.get(img[i][j], 0)
            hstg[img[i][j]] = c + 1
    return hstg

def histogram_equalization(img):
    L = 256
    M, N = img.shape[0], img.shape[1]
    hstg = compute_historgram(img)
    T = {}
    s = 0.0
    for gray_level in range(256):
        s += hstg.get(gray_level, 0)
        T[gray_level] = (L-1) * s / (M * N)

    hstg_img = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            hstg_img[i][j] = T[img[i][j]]

    return hstg_img

def main():
    img_file = 'Fig0308(a)(fractured_spine).tif'

    img = misc.imread(img_file)

# taks (a)
    hstg = compute_historgram(img)

    for key in hstg.keys():

        print key, hstg[key]

# task (b)
    htsg_img = histogram_equalization(img)
    

    misc.imsave('hstg_%s' % img_file, htsg_img)

if __name__ == '__main__':
    main()
