#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''
import sys
import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

sys.path.append('../Proj03-03/')

from spatial_filtering import spatial_filtering

def laplacian_enhancement(img):

    mask = numpy.array([[0, 1, 0],
            [1,-4, 1],
            [0, 1, 0]])

    processed_img = spatial_filtering(img, mask)

    return processed_img

def main():
    img_file = 'Fig0338(a)(blurry_moon).tif'
    img = misc.imread(img_file)

    processed_img = img-laplacian_enhancement(img)

    misc.imsave('laplacian_enhanced_%s' % img_file, processed_img)

if __name__ == '__main__':
    main()
