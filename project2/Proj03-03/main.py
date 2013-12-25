#!/bin/python
# *-* encoding=utf-8 *-*

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

def spatial_filtering(img, func):
    def f(x, y):
        if x >= 0 and x < M and \
           y >= 0 and y < N:
            return img[x][y]
        else:
            return 0

    processed_img = img.copy()

    return processed_img

def apply_mask(img):
    mask = numpy.array([[0,0,0],[0,1,0],[0,0,0]])

def main():
    img_file = 'Fig0338(a)(blurry_moon).tif'
    img = misc.imread(img_file)

    processed_img = laplacian_enhancement(img)

    misc.imsave('laplacian_enhanced_%s' % img_file, processed_img)

if __name__ == '__main__':
    main()
