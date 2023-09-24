from PIL import Image
from numpy import asarray, newaxis
import matplotlib.pyplot as plt
from load_image import ft_load


def crop_image(img: Image.Image, zoom_size=(400, 400)) -> Image.Image:
    """Crop the center of an image using Pillow."""
    width, height = img.size
    left = (width - zoom_size[0]) // 2
    top = (height - zoom_size[1]) // 2
    right = left + zoom_size[0]
    bottom = top + zoom_size[1]
    return img.crop((left, top, right, bottom))


def convert_to_grayscale(img: Image.Image) -> asarray:
    """Convert an image to grayscale using Pillow and maintain 3D shape."""
    grayscale_img = img.convert("L")
    grayscale_array = asarray(grayscale_img)
    grayscale_array = grayscale_array[:, :, newaxis]
    return grayscale_array


def display_image_with_scale(img_array):
    """Display the image with scale on x and y axes."""
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(img_array.squeeze(), cmap='gray')
    ax.set_xticks(range(0, img_array.shape[1], 50))
    ax.set_yticks(range(0, img_array.shape[0], 50))
    plt.show()


if __name__ == "__main__":
    try:
        img_array = ft_load("animal.jpeg")
        img = Image.fromarray(img_array)
        print(asarray(img))
        cropped_img = crop_image(img)
        grayscale_array_3d = convert_to_grayscale(cropped_img)
        print(f"New shape after slicing: {grayscale_array_3d.shape}")
        print(grayscale_array_3d)
        display_image_with_scale(grayscale_array_3d)
    except Exception as e:
        print(str(e))
