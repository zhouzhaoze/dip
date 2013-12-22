# *-* encoding=utf-8 *-*
import sys
import scipy
import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

def reduce_gray_level_resolution(image, level):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            #image[i][j] = np.int8(image[i][j] / 255.0 * level)
            # with scaling? expand the range [0,1] to [0, 255]
            image[i][j] = np.int8(int(image[i][j] / 255.0 * level) * 256/level)

    return image

def read_and_write_lena():
    lena = misc.imread('lena.bmp')

    if len(sys.argv) < 2:
        print 'Usage: %s [gray_level]\n' % sys.argv[0]
        return

    gray_level = int(sys.argv[1])
    lena = reduce_gray_level_resolution(lena, gray_level)

    plt.figure()
    plt.imshow(lena, cmap=plt.cm.gray)
    plt.show()

    misc.imsave('lena_gray_level-%d.bmp' % gray_level, lena)

if __name__ == '__main__':
    #f()
    read_and_write_lena()
