#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

ht_map = {
        0: numpy.array([[0,0,0],
                          [0,0,0],
                          [0,0,0]]),
        1: numpy.array([[0,1,0],
                          [0,0,0],
                          [0,0,0]]),
        2: numpy.array([[0,1,0],
                          [0,0,0],
                          [0,0,1]]),
        3: numpy.array([[1,1,0],
                          [0,0,0],
                          [0,0,1]]),
        4: numpy.array([[1,1,0],
                          [0,0,0],
                          [1,0,1]]),
        5: numpy.array([[1,1,1],
                          [0,0,0],
                          [1,0,1]]),
        6: numpy.array([[1,1,1],
                          [0,0,1],
                          [1,0,1]]),
        7: numpy.array([[1,1,1],
                          [0,0,1],
                          [1,1,1]]),
        8: numpy.array([[1,1,1],
                          [1,0,1],
                          [1,1,1]]),
        9: numpy.array([[1,1,1],
                          [1,1,1],
                          [1,1,1]])
        }


'''
f(x) = (x - min_val) / range * 9
'''
def halftoning(img):
    max_val = numpy.max(img)
    min_val = numpy.min(img)
    rg = (max_val - min_val) 
    print max_val, min_val, rg

    ht_img = img.copy()

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            ht_img[i][j] = img[i][j] / 256.0 * 10

    img = ht_img

    #return img

    htimg = numpy.zeros(3*img.shape[0] * 3*img.shape[1]).reshape(img.shape[0]*3, img.shape[1]*3)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            v = int(img[i][j])
            for ii in range(3):
                for jj in range(3):
        #            print v
                    htimg[i*3 + ii][j*3 + jj] = ht_map[v][ii][jj] / 9.0 * 256
#    print

    return htimg

def task_b():
    a = numpy.zeros(256*256).reshape(256, 256)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a[i][j] = i;

    ht_img = halftoning(a)
    plt.figure()
    plt.imshow(ht_img, cmap=plt.cm.gray)
    plt.show()

    misc.imsave('ht_a.bmp', ht_img)

def main():
    img_file = 'Fig0222(a)(face).tif'

    img = misc.imread(img_file)

    ht_img = halftoning(img)

#    plt.figure()
#    plt.imshow(img, cmap=plt.cm.gray)
#    plt.show()

    misc.imsave('ht_%s' % img_file, ht_img)

if __name__ == '__main__':
    #task_b()
    main()
