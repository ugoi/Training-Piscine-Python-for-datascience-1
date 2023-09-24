from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt
from load_image import ft_load


def center_crop(img_array, desired_size):
    """
    Center crop an image array to the specified size.

    Parameters:
    - img_array (numpy.ndarray): Input image array.
    - desired_size (int): Desired size for both height and width after
cropping.

    Returns:
    - numpy.ndarray: Center-cropped image array.
    """
    offset_x = (img_array.shape[0] - desired_size) // 2
    offset_y = (img_array.shape[1] - desired_size) // 2
    return img_array[offset_x:offset_x+desired_size,
                     offset_y:offset_y+desired_size]


if __name__ == "__main__":
    try:
        img_array = ft_load("animal.jpeg")
        print(img_array)
        img = Image.fromarray(img_array)
        grayscale_img = img.convert("L")
        img_array = asarray(grayscale_img)
        cropped_img = center_crop(img_array, 400)
        print(f"New shape after slicing: {cropped_img.shape}")
        print(cropped_img)
        plt.figure(figsize=(8, 8))
        plt.imshow(cropped_img, cmap='gray')
        plt.show()
    except Exception as e:
        print(str(e))
