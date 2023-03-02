from format_converter import *
from SSIM import ssim_compare
from PSNR import psnr_compare
from compression_rate import get_compression_rate
import os

images_path = "images/"
jpeg_path = "jpeg_images/"
jpeg2000_path = "jpeg2000_images/"


def remove_transparency(image_path):
    Image.open(image_path).convert("RGB").save(image_path)


def main():
    image_names = os.listdir(images_path)
    for name in image_names:
        curr_image = images_path + name
        curr_jpeg_path = jpeg_path + name.replace(".png", ".jpg")
        curr_jpeg2000_path = jpeg2000_path + name.replace(".png", ".jp2")

        remove_transparency(curr_image)
        convert_to_jpeg(curr_image, curr_jpeg_path)
        convert_to_jpeg2000(curr_image, curr_jpeg2000_path)

        ssim_jpeg = ssim_compare(curr_image, curr_jpeg_path)
        psnr_jpeg = psnr_compare(curr_image, curr_jpeg_path)
        compression_rate_jpeg = get_compression_rate(curr_image, curr_jpeg_path)

        ssim_jpeg2000 = ssim_compare(curr_image, curr_jpeg2000_path)
        psnr_jpeg2000 = psnr_compare(curr_image, curr_jpeg2000_path)
        compression_rate_jpeg2000 = get_compression_rate(curr_image, curr_jpeg2000_path)

        print(name + ": \n")
        print("Jpeg: ")
        print(f"SSIM: {ssim_jpeg}")
        print(f"PSNR: {psnr_jpeg}")
        print(f"Taux de compression: {compression_rate_jpeg} \n")

        print("Jpeg2000: ")
        print(f"SSIM: {ssim_jpeg2000}")
        print(f"PSNR: {psnr_jpeg2000}")
        print(f"Taux de compression: {compression_rate_jpeg2000} \n")


if __name__ == "__main__":
    main()