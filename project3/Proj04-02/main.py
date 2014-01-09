#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import sys
import numpy, scipy
from scipy import ndimage
from scipy import misc
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

sys.path.append('../Proj04-01')

from DFT import DFT_2D, IDFT_2D


def main():
    img_file = 'Fig0441(a)(characters_test_pattern).tif'
    img = misc.imread(img_file)

    processed_img = DFT_2D(img)
    display_img = fftpack.fftshift(processed_img)
    display_img = numpy.abs(display_img) 
    display_img = numpy.log(display_img+1)

    idtft_img = IDFT_2D(processed_img).real

    misc.imsave('fft_%s' % (img_file), display_img)
    misc.imsave('idtft_%s' % (img_file), idtft_img)

if __name__ == '__main__':
    main()
