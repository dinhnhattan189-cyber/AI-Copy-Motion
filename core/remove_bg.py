from rembg import remove
from PIL import Image


def remove_background(input_path, output_path):
    """
    Xóa nền ảnh bằng rembg.
    """

    input_image = Image.open(input_path)

    output_image = remove(input_image)

    output_image.save(output_path)

    return output_path