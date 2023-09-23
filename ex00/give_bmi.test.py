import unittest
from give_bmi import give_bmi, apply_limit

class TestBMIFunctions(unittest.TestCase):

    def test_give_bmi(self):
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        self.assertEqual(give_bmi(height, weight), [22.507863455018317, 29.0359168241966])

    def test_apply_limit(self):
        bmi_values = [22.507863455018317, 29.0359168241966]
        self.assertEqual(apply_limit(bmi_values, 26), [False, True])

    def test_mismatched_lists(self):
        with self.assertRaises(ValueError):
            give_bmi([1.75], [70, 80])

    def test_wrong_data_type(self):
        with self.assertRaises(ValueError):
            give_bmi([1.75, '1.80'], [70, 80])

        with self.assertRaises(ValueError):
            apply_limit([22.5, "24.5"], 25)

        with self.assertRaises(ValueError):
            apply_limit([22.5, 24.5], "25")

if __name__ == '__main__':
    unittest.main()
