import unittest
from load_image import ft_load
import numpy as np

class TestFtLoadFunction(unittest.TestCase):
    
    # Test loading of a valid image
    def test_valid_image(self):
        result = ft_load("cat.jpg")
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(len(result.shape), 3)  # Ensure it's a 3D array (height, width, channels)
        
    # Test invalid image path
    def test_invalid_image_path(self):
        with self.assertRaises(Exception) as context:
            ft_load("nonexistent.jpg")
        self.assertIn("Error:", str(context.exception))
        
    # Test non-JPG/JPEG formats
    def test_non_jpg_format(self):
        result = ft_load("landscape.png")
        self.assertIsInstance(result, np.ndarray)
    
    # Test an invalid format (like a text file)
    def test_invalid_format(self):
        with open("test.txt", "w") as f:
            f.write("This is not an image")
        with self.assertRaises(Exception) as context:
            ft_load("test.txt")
        self.assertIn("Error:", str(context.exception))

# This allows the tests to be run from the command line using python -m unittest test_load_image.py
if __name__ == "__main__":
    unittest.main()
