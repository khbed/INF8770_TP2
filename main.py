#!/usr/bin/env python3

from SSIM import ssim_compare
from PSNR import psnr_compare
from compression_rate import get_compression_rate
import os
import cv2

os.environ['OPENCV_IO_ENABLE_JASPER'] = 'true'

images_path = "images/"
jpeg_path = "jpeg_images/"
jpeg2000_path = "jpeg2000_images/"

if not os.path.exists(jpeg_path):
   os.makedirs(jpeg_path)
if not os.path.exists(jpeg2000_path):
   os.makedirs(jpeg2000_path)

def remove_transparency(image_path):
    image = cv2.imread(image_path)
    new_image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    cv2.imwrite(image_path, new_image)

def convert_image(path_name, new_path):
    image = cv2.imread(path_name, cv2.IMREAD_COLOR)
    cv2.imwrite(new_path, image)

def main():
    image_names = os.listdir(images_path)
    for name in image_names:
        curr_image = images_path + name
        curr_jpeg_path = jpeg_path + name.replace(".png", ".jpg")
        curr_jpeg2000_path = jpeg2000_path + name.replace(".png", ".jp2")

        remove_transparency(curr_image)
        convert_image(curr_image, curr_jpeg_path)
        convert_image(curr_image, curr_jpeg2000_path)

        ssim_jpeg = ssim_compare(curr_image, curr_jpeg_path)
        psnr_jpeg = psnr_compare(curr_image, curr_jpeg_path)
        compression_rate_jpeg = get_compression_rate(curr_image, curr_jpeg_path)

        ssim_jpeg2000 = ssim_compare(curr_image, curr_jpeg2000_path)
        psnr_jpeg2000 = psnr_compare(curr_image, curr_jpeg2000_path)
        compression_rate_jpeg2000 = get_compression_rate(curr_image, curr_jpeg2000_path)

        print(name + ": \n")
        print("Jpeg: ")
        print(f"SSIM: {ssim_jpeg}")
        print(f"PSNR: {psnr_jpeg} dB")
        print(f"Taux de compression: {compression_rate_jpeg} \n")

        print("Jpeg2000: ")
        print(f"SSIM: {ssim_jpeg2000}")
        print(f"PSNR: {psnr_jpeg2000} dB")
        print(f"Taux de compression: {compression_rate_jpeg2000} \n")


if __name__ == "__main__":
    main()
