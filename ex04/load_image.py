from PIL import Image
from numpy import asarray
import numpy as np


def ft_load(path: str) -> any:
    """Load an image, convert to grayscale.

    Parameters:
    - path (str): The path to the image file.

    Returns:
    - numpy array: Pixel content in grayscale format.
    - str: Error message if an issue occurs while loading the image.
    """
    try:
        img = Image.open(path)
        grayscale_img = img.convert("L")
        width, height = grayscale_img.size
        center_x, center_y = width // 2, height // 2
        left = center_x - 200
        upper = center_y - 200
        right = center_x + 200
        lower = center_y + 200
        cropped_img = grayscale_img.crop((left, upper, right, lower))
        img_array = asarray(cropped_img)
        img_array_3d = img_array[:, :, np.newaxis]
        print(f"The shape of cropped grayscale image is: {img_array_3d.shape}")
        return img_array_3d
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
