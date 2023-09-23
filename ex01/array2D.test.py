import unittest
from array2D import slice_me
import io
import sys

class TestSliceMeFunction(unittest.TestCase):

    def setUp(self):
        self.family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]

    def test_valid_input(self):
        # Redirect stdout to capture print statements
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Test valid input
        result = slice_me(self.family, 0, 2)
        expected_output = "My shape is : (4, 2)\nMy new shape is : (2, 2)\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        self.assertEqual(result, [[1.8, 78.4], [2.15, 102.7]])

        # Reset captured_output
        captured_output.truncate(0)
        captured_output.seek(0)

        result = slice_me(self.family, 1, -2)
        expected_output = "My shape is : (4, 2)\nMy new shape is : (1, 2)\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
        self.assertEqual(result, [[2.15, 102.7]])

        # Restore stdout
        sys.stdout = sys.__stdout__

    def test_invalid_input(self):
        # Test non-list input
        with self.assertRaises(ValueError):
            slice_me("invalid", 0, 2)

        # Test if sublists contain non-numeric values
        invalid_family2 = [
            "[1.80, 78.4]",
            [2.15, 102.7]
        ]
        with self.assertRaises(ValueError):
            slice_me(invalid_family2, 0, 2)

        # Test uneven list
        uneven_family = [
            [1.80, 78.4, 100],
            [2.15, 102.7]
        ]
        with self.assertRaises(ValueError):
            slice_me(uneven_family, 0, 2)

        # Test non-2D input
        non_2d_family = [1.80, 2.15]
        with self.assertRaises(ValueError):
            slice_me(non_2d_family, 0, 2)

if __name__ == '__main__':
    unittest.main()
