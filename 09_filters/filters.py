import numpy as np

BLUR_3x3 = (1/9) * np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

SHARPEN = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

EDGE = np.array([
    [-1,-1,-1],
    [-1,8,-1],
    [-1,-1,-1]
])

EMBOSS = np.array([
    [-2,-1,0],
    [-1,1,1],
    [0,1,2]
])
