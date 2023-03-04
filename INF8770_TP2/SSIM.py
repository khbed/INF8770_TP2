# https://code.adonline.id.au/structural-similarity-index-ssim-in-python/

from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2

def ssim_compare(original_image, compressed_image): 

    # Import images
    image1 = cv2.imread(original_image)
    image2 = cv2.imread(compressed_image, 1)

    # Convert the images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Check for same size and ratio and report accordingly
    ho, wo, _ = image1.shape
    hc, wc, _ = image2.shape
    ratio_orig = ho/wo
    ratio_comp = hc/wc
    dim = (wc, hc)

    if round(ratio_orig, 2) != round(ratio_comp, 2):
        print("\nImages not of the same dimension. Check input.")
        exit()

    # Resize first image if the second image is smaller
    elif ho > hc and wo > wc:
        print("\nResizing original image for analysis...")
        gray1 = cv2.resize(gray1, dim)

    elif ho < hc and wo < wc:
        print("\nCompressed image has a larger dimension than the original. Check input.")
        exit()

    if round(ratio_orig, 2) == round(ratio_comp, 2):
        return ssim(gray1, gray2)
