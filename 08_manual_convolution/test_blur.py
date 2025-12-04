import cv2
import numpy as np
from manual_convolution import convolve
from kernels import BLUR_KERNEL


img = cv2.imread('../data/lena.png', 0)


blurred = convolve(img, BLUR_KERNEL)


cv2.imwrite('blurred_lena.png', blurred)
print("Saved blurred_lena.png")

