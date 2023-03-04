# https://www.geeksforgeeks.org/python-peak-signal-to-noise-ratio-psnr/

from math import log10, sqrt
import cv2
import numpy as np

def psnr_compare(original_image, compressed_image):
    original = cv2.imread(original_image)
    compressed = cv2.imread(compressed_image, 1)

    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))

    return psnr
