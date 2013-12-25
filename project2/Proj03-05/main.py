#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt


def highboost_enhancement(img, A):
    def f(x, y):
        if x >= 0 and x < M and \
           y >= 0 and y < N:
            return img[x][y]
        else:
            return 0

    M, N = img.shape

    mask = [[0, 1, 0],
            [1,-4, 1],
            [0, 1, 0]]

    processed_img = numpy.zeros(M * N).reshape(M, N)
    #processed_img = img.copy() * A

    for i in range(M):
        for j in range(N):
            for ii in range(3):
                for jj in range(3):
                    processed_img[i][j] += f(i+ii-1, j+jj-1) * mask[ii][jj]

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
