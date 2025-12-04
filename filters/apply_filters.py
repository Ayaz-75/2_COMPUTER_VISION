import cv2
 
from ..08_manual_convolution.manual_convolution import convolve
from filters import BLUR_3x3, SHARPEN, EDGE, EMBOSS

def apply_all_filters(image_path):
    img = cv2.imread(image_path, 0)

    output = {
        "blur": convolve(img, BLUR_3x3),
        "sharpen": convolve(img, SHARPEN),
        "edge": convolve(img, EDGE),
        "emboss": convolve(img, EMBOSS)
    }

    return output
