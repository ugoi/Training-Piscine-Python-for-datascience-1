import numpy as np
import matplotlib.pyplot as plt


def display(array):
    '''Displays array.'''
    plt.imshow(array)
    plt.axis('off')
    plt.show()


def ft_invert(array: np.ndarray) -> np.ndarray:
    '''Inverts the color of the image received.'''
    result = 255 - array
    display(result.astype(np.uint8))
    return result


def ft_red(array: np.ndarray) -> np.ndarray:
    '''Keeps only the red channel of the image.'''
    red_array = array.copy()
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    display(red_array.astype(np.uint8))
    return red_array


def ft_green(array: np.ndarray) -> np.ndarray:
    '''Keeps only the green channel of the image.'''
    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    display(green_array.astype(np.uint8))
    return green_array


def ft_blue(array: np.ndarray) -> np.ndarray:
    '''Keeps only the blue channel of the image.'''
    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    display(blue_array.astype(np.uint8))
    return blue_array


def ft_grey(array: np.ndarray) -> np.ndarray:
    '''Converts the image to greyscale.'''
    grey_array = np.mean(array, axis=2, keepdims=True) / 3
    grey_image = np.concatenate([grey_array, grey_array, grey_array], axis=2)
    display(grey_image.astype(np.uint8))
    return grey_image
