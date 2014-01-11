#!/bin/python
# *-* encoding=utf-8 *-*

import sys
import math
import numpy, scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import random
import colorsys

sys.path.append('../../project2/Proj03-02')

from histogram_equalization import histogram_equalization

import math

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b
    
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

def hist_RGB(img):
    M, N = img.shape[0], img.shape[1]
    R = numpy.zeros(M*N).reshape((M, N))
    G = numpy.zeros(M*N).reshape((M, N))
    B = numpy.zeros(M*N).reshape((M, N))
    for i in range(M):
        for j in range(N):
            R[i][j], G[i][j], B[i][j] = img[i][j]

    processed_img = img.copy()

    R = histogram_equalization(R)
    G = histogram_equalization(G)
    B = histogram_equalization(B)

    for i in range(M):
        for j in range(N):
            processed_img[i][j] = R[i][j], G[i][j], B[i][j]

    return processed_img

def hist_intensity(img):
    M, N = img.shape[0], img.shape[1]
    H = numpy.zeros(M*N).reshape((M, N))
    S = numpy.zeros(M*N).reshape((M, N))
    I = numpy.zeros(M*N).reshape((M, N))
    for i in range(M):
        for j in range(N):
            r, g, b = img[i][j]
            H[i][j], I[i][j], S[i][j] = colorsys.rgb_to_hls(r, g, b)

    I = 255 * I
    I = histogram_equalization(I)

    processed_img = img.copy()

    for i in range(M):
        for j in range(N):
            processed_img[i][j] = colorsys.hls_to_rgb(H[i][j], I[i][j], S[i][j])

    return processed_img

def main():
    img_file = 'Fig0635(top_ left_flower).tif'

    img = misc.imread(img_file)


    processed_img = hist_RGB(img)
    misc.imsave('hist_RGB_%s' % img_file, processed_img)

    processed_img = hist_intensity(img)
    misc.imsave('hist_intensity_%s' % img_file, processed_img)

if __name__ == '__main__':
    main()
