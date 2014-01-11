#!/bin/python
# *-* encoding=utf-8 *-*
'''
Image Priting Program Based on Haftoning
'''

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import random


def gaussian_noise_gen(mean, var):
    def f(val):
        return val + random.gauss(mean, var)
    return f

def salt_and_pepper_noise_gen(val_a, p_a, val_b, p_b):
    def f(val):
        a = random.random()
        if a < p_a:
            return val_a
        elif a < p_a + p_b:
            return val_b
        else:
            return val
    return f

def en_noise(img, noise_generator):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] = noise_generator(img[i][j])
    return img

def laplacian_enhancement(img):
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

    for i in range(M):
        for j in range(N):
            for ii in range(3):
                for jj in range(3):
                    processed_img[i][j] += f(i+ii-1, j+jj-1) * mask[ii][jj]

    return processed_img

def main():
    img_file = 'Fig0507(a)(ckt-board-orig).tif'

    img = misc.imread(img_file)

#    processed_img = en_noise(img, gaussian_noise_gen(0, 1))
    processed_img = en_noise(img, salt_and_pepper_noise_gen(0, 0.2, 255, 0.2))

    misc.imsave('gaussian_noise_%s' % img_file, processed_img)

if __name__ == '__main__':
    main()
