from PIL import Image
from numpy import asarray


def ft_load(path: str) -> any:
    """Load an image, print its 3D dimensions, and return its pixel content.

    Parameters:
    - path (str): The path to the image file.

    Returns:
    - numpy array: Pixel content in RGB format.
    - str: Error message if an issue occurs while loading the image.
    """
    try:
        # Load the image
        img = Image.open(path)

        # Convert the image to a numpy array
        img_array = asarray(img)

        # Print the shape of the numpy array
        print(f"The shape of image is: {img_array.shape}")

        return img_array
    except Exception as e:
        # Handle any error with a clear message
        return f"Error: {str(e)}"
