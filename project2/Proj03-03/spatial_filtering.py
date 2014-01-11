#!/bin/python
# *-* encoding=utf-8 *-*

import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

def spatial_filtering(img, mask):
    M, N = img.shape
    M1, N1 = mask.shape
    M1, N1 = M1/2, N1/2

    from_img = numpy.zeros((M+M1*2)*(N+N1*2)).reshape((M+M1*2, N+N1*2))
    to_img =   numpy.zeros((M+M1*2)*(N+N1*2)).reshape((M+M1*2, N+N1*2))

    for i in range(M):
        for j in range(N):
            from_img[i+M1][j+N1] = img[i][j]

    for i in range(M):
        for j in range(N):
            for ii in range(mask.shape[0]):
                for jj in range(mask.shape[1]):
                    to_img[i+M1][j+N1] += from_img[i+ii][j+jj] * mask[ii][jj]

    return to_img[M1:M1+M,N1:N1+N]

def main():
    img_file = 'Fig0338(a)(blurry_moon).tif'
    img = misc.imread(img_file)

    processed_img = spatial_filtering(img, mask=numpy.array([[0,1,0],[1,-4,1],[0,1,0]]))

    misc.imsave('processed_%s' % img_file, processed_img)

if __name__ == '__main__':
    main()
