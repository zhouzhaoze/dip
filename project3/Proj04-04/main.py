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

def en_padding(img):
    M, N = img.shape
    P, Q = 2 * M, 2 * N
    _img = numpy.zeros(P*Q).reshape((P, Q))
    for x in range(M):
        for y in range(N):
            _img[x][y] = img[x][y]
    return _img

def de_padding(img):
    P, Q = img.shape
    M, N = P/2, Q/2
    _img = numpy.zeros(M*N).reshape((M, N))
    for x in range(M):
        for y in range(N):
            _img[x][y] = img[x][y]
    return _img

def shift(img):
    M, N = img.shape
    _img = img.copy()
    for x in range(M):
        for y in range(N):
            _img[x][y] = img[x][y] * numpy.power(-1.0, (x+y))
    return _img

def sqdistance(p1, p2):
    return ((p1[0]-p2[0])*(p1[0]-p2[0])) + \
           ((p1[1]-p2[1])*(p1[1]-p2[1]))

def lowpass_mask(P, Q, cuf_off_frequency):
    center = (P/2.0, Q/2.0)
    mask = numpy.zeros(P * Q).reshape(P, Q)
    for u in range(P):
        for v in range(Q):
            mask[u][v] = numpy.exp(-1*sqdistance(center, (u, v)) / (2*(cuf_off_frequency*cuf_off_frequency)))
    return mask

def highpass_mask(P, Q, cuf_off_frequency):
    return 1.0 - lowpass_mask(P, Q, cuf_off_frequency)
#    center = (P/2.0, Q/2.0)
#    mask = numpy.zeros(P * Q).reshape(P, Q)
 #  for u in range(P):
#        for v in range(Q):
#            mask[u][v] = 1.0-numpy.exp(-1*sqdistance(center, (u, v)) / (2*(cuf_off_frequency*cuf_off_frequency)))
#    return mask

def main():
    img_file = 'Fig0441(a)(characters_test_pattern).tif'
    img = misc.imread(img_file)

    padding_img = en_padding(img)

    padding_img = shift(padding_img)

    dft_img = DFT_2D(padding_img)

    for cut_off_frequency in [30, 60, 160]:
        print cut_off_frequency
        hp_mask = highpass_mask(dft_img.shape[0], dft_img.shape[1], cut_off_frequency)
        
        misc.imsave('%s_hpmask_%d.tif' % (img_file, cut_off_frequency), 255 * hp_mask)
        hp_img  = numpy.multiply(dft_img, hp_mask)

        misc.imsave('%s_fft_%d.tif' % (img_file, cut_off_frequency), numpy.log(1+numpy.abs(hp_img)))
     
        hp_idtft_img = shift(IDFT_2D(hp_img).real)
        hp_idtft_img = de_padding(hp_idtft_img)
        print hp_idtft_img.shape
        misc.imsave('%s_hp_%d.tif' % (img_file, cut_off_frequency), hp_idtft_img)

if __name__ == '__main__':
    main()
