# *-* encoding=utf-8 *-*
import sys
import scipy
import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

def reduce_spatial_resolution(image, width):
    reduce_image = np.zeros(width * width).reshape(width, width)

    scale = image.shape[0] / width

    for i in range(reduce_image.shape[0]):
        for j in range(reduce_image.shape[1]):
#            print i, j
            for ii in range(scale):
                for jj in range(scale):
                    reduce_image[i][j] += image[scale*i + ii][scale*j + jj]
            reduce_image[i][j] /= scale * scale
    return reduce_image

def read_and_write_lena():
    lena = misc.imread('lena.bmp')

    width = 16
    lena2 = reduce_spatial_resolution(lena, width)
    misc.imsave('lena_spatial_resolution_reduction-%d.bmp' % width, lena2)

if __name__ == '__main__':
    #f()
    read_and_write_lena()
