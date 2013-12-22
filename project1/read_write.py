# *-* encoding=utf-8 *-*
import scipy
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

def read_and_write_lena():
    lena = misc.imread('lena.bmp')

    plt.figure()
    plt.imshow(lena, cmap=plt.cm.gray)
    plt.show()

    misc.imsave('lena_copy.bmp', lena)

if __name__ == '__main__':
    #f()
    read_and_write_lena()
