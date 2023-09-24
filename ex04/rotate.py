import numpy as np
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


def transpose_image(img_array):
    """
    Transpose an image array by flipping its axes.

    Parameters:
    - img_array (numpy.ndarray): Input image array.

    Returns:
    - numpy.ndarray: Transposed image array.
    """
    transposed = np.zeros((img_array.shape[1], img_array.shape[0]),
                          dtype=img_array.dtype)
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            transposed[j][i] = img_array[i][j]
    return transposed


def main():
    img_array = ft_load("animal.jpeg")
    print(img_array)

    if len(img_array.shape) == 3 and img_array.shape[2] > 1:
        img_array = img_array[:, :, 0]

    cropped_img = center_crop(img_array, 400)

    transposed_img = transpose_image(cropped_img)

    plt.figure(figsize=(8, 8))
    plt.imshow(transposed_img, cmap='gray')
    plt.show()

    print(f"New shape after Transpose: {transposed_img.shape}")
    print(transposed_img)


if __name__ == '__main__':
    main()
