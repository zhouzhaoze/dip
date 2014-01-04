#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt


def fft(img):
    print img.shape



def main():
    img_file = 'Fig0441(a)(characters_test_pattern).tif'
    img = misc.imread(img_file)

    fft(img)

    #misc.imsave('highboost_A%f_enhanced_%s' % (A, img_file), processed_img)

if __name__ == '__main__':
    main()
