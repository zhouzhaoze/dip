#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import numpy, scipy
from scipy import ndimage
from scipy import misc
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

'''
def DFT_matrix(N):
    i, j = numpy.meshgrid(numpy.arange(N), numpy.arange(N))
    omega = numpy.exp(-2*numpy.pi*1J/N)
    W = numpy.power(omega, i * j) / numpy.sqrt(N)
    return W

def DFT_matrix_2d(x):
    M, N = x.shape
    W1 = DFT_matrix(M)
    W2 = DFT_matrix(N)

    fft_of_x = numpy.dot(W1, x)
    fft_of_x = numpy.dot(fft_of_x, W2)

    return fft_of_x
'''
def DFT_2D(img):
    M, N = img.shape
    _m = numpy.array(numpy.arange(M))
    MM = numpy.outer(_m, _m)
    omega = numpy.exp(-2*numpy.pi*1J/M)
    MM = numpy.power(omega, MM) 

    _n = numpy.array(numpy.arange(N))
    NN = numpy.outer(_n, _n)
    omega = numpy.exp(-2*numpy.pi*1J/N)
    NN = numpy.power(omega, NN)

    ret = img

    ret = numpy.dot(MM, ret)
    ret = numpy.dot(ret, NN)
    return ret

def IDFT_2D(img):
    M, N = img.shape
    _m = numpy.array(numpy.arange(M))
    MM = numpy.outer(_m, _m)
    omega = numpy.exp(2*numpy.pi*1J/M)
    MM = numpy.power(omega, MM) / (M*N) 

    _n = numpy.array(numpy.arange(N))
    NN = numpy.outer(_n, _n)
    omega = numpy.exp(2*numpy.pi*1J/N)
    NN = numpy.power(omega, NN) / (M*N)

    ret = img

    ret = numpy.dot(MM, ret)
    ret = numpy.dot(ret, NN)
    return ret



def shift_img(img):
    M, N = img.shape
    for i in range(M):
        for j in range(N):
           img[i][j] *= (-1.0)**(i+j)
    return img

def main():
    img_file = 'Fig0441(a)(characters_test_pattern).tif'
#    img_file = 'Fig0421(car_newsprint_sampled_at_75DPI).tif'
#    img_file = 'Fig0425(a)(translated_rectangle).tif'
#    img_file = 'Fig0424(a)(rectangle).tif'
    img = misc.imread(img_file)

#    img = shift_img(img)
    processed_img = DFT_2D(img)
#    processed_img = fftpack.fft2(img)
    display_img = fftpack.fftshift(processed_img)
    display_img = numpy.abs(display_img) 
    display_img = numpy.log(display_img+1)

#    plt.figure()
#    plt.imshow(processed_img, cmap=plt.cm.gray)
#    plt.show()
    idtft_img = IDFT_2D(processed_img).real

    misc.imsave('fft_%s' % (img_file), display_img)
    misc.imsave('idtft_%s' % (img_file), idtft_img)

if __name__ == '__main__':
    main()
