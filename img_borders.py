import os
import cv2
import sys
from multiprocessing import Pool
import numpy as np


def normalize(img):
    vmin = img.min()
    vmax = img.max()

    img = (img - vmin) / vmax * 255


def _border3(src, kernel_x, kernel_y):
    out = np.zeros(src.shape, src.dtype)

    rows, cols = src.shape[:2]

    for i in range(1, rows-1):
        r0 = i - 1
        r1 = i + 2
        for j in range(1, cols - 1):
            c0 = j - 1
            c1 = j + 2
            window = src[r0:r1, c0: c1]
            outx = abs((window * kernel_x).sum())
            outy = abs((window * kernel_y).sum())
            out[i, j] = min(255, outx + outy)

    return out


def sobel(src):
    kernel_x = np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ])
    kernel_y = np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ])
    return _border3(src, kernel_x, kernel_y)


def prewitt(src):
    kernel_x = np.array([
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ])
    kernel_y = np.array([
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ])
    return _border3(src, kernel_x, kernel_y)


def roberts(src):
    out = np.zeros(src.shape, src.dtype)
    kernel_x = np.array([
        [-1, 0],
        [0, 1],
    ])
    kernel_y = np.array([
        [0, -1],
        [1, 0],
    ])

    rows, cols = src.shape[:2]

    for i in range(1, rows-1):
        r0 = i - 1
        r1 = i + 1
        for j in range(1, cols - 1):
            c0 = j - 1
            c1 = j + 1
            window = src[r0:r1, c0: c1]
            outx = abs((window * kernel_x).sum())
            outy = abs((window * kernel_y).sum())
            out[i, j] = min(255, outx + outy)

    return out


def laplace(src):
    out = np.zeros(src.shape, src.dtype)
    kernel = np.array([
        [0, 1, 0],
        [1, -4, 1],
        [0, 1, 0]
    ])

    rows, cols = src.shape[:2]

    for i in range(1, rows-1):
        r0 = i - 1
        r1 = i + 2
        for j in range(1, cols - 1):
            c0 = j - 1
            c1 = j + 2
            window = src[r0:r1, c0: c1]
            out_tmp = abs((window * kernel).sum())
            out[i, j] = min(255, out_tmp)

    return out

