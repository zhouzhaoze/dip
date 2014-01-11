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

    print M+M1*2
    print N+N1*2

    from_img = numpy.zeros((M+M1*2)*(N+N1*2)).reshape((M+M1*2, N+N1*2))
    to_img =   numpy.zeros((M+M1*2)*(N+N1*2)).reshape((M+M1*2, N+N1*2))

    for i in range(M):
        for j in range(N):
            from_img[i+M1][j+N1] = img[i][j]

    to_img = from_img.copy()

    for i in range(M):
        for j in range(N):
            tmp = []
            for ii in range(mask.shape[0]):
                for jj in range(mask.shape[1]):
                    tmp.append(from_img[i+ii][j+jj])
            tmp = numpy.sort(tmp)
            to_img[i+M1][j+N1] = tmp[(mask.shape[0]*mask.shape[1])/2+1]

    return to_img[M1:M1+M, N1:N1+N]

def main():
    img_file = 'Fig0338(a)(blurry_moon).tif'
    img_file = 'gaussian_noise_Fig0507(a)(ckt-board-orig).tif'
    img = misc.imread(img_file)

    processed_img = spatial_filtering(img, mask=numpy.zeros(3*3).reshape((3, 3)))

    misc.imsave('processed_%s' % img_file, processed_img)

if __name__ == '__main__':
    main()
