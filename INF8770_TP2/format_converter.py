from PIL import Image


def convert_to_jpeg(path_name, new_path):
    original_image = Image.open(path_name)
    original_image.convert('RGB').save(new_path, "JPEG")
    return new_path

def convert_to_jpeg2000(path_name, new_path):
    original_image = Image.open(path_name)
    original_image.convert('RGB').save(new_path, "JPEG2000")
    return new_path
    
