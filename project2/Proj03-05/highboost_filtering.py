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

def highboost_enhancement(img, A):
    M, N = img.shape

    mask = numpy.array([[0, 1, 0], [1,-4, 1], [0, 1, 0]])

    processed_img = spatial_filtering(img, mask)

    processed_img = img * A - processed_img

    return processed_img

def main():
    img_file = 'Fig0338(a)(blurry_moon).tif'
    img_file = 'Fig0340(a)(dipxe_text).tif'
    img = misc.imread(img_file)

    A = 1.7

    for A in [1, 1.2, 1.3, 1.7, 2.0, 3.0, 4]:

        processed_img = highboost_enhancement(img, A)

        misc.imsave('highboost_A%f_enhanced_%s' % (A, img_file), processed_img)

if __name__ == '__main__':
    main()
