import numpy as np

BLUR_KERNEL = (1/9) * np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

SHARPEN_KERNEL = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
