import unittest
from sort import sort


class TestSortFunction(unittest.TestCase):
    def setUp(self):
        # Define common test values
        self.standard_dimensions = (50, 50, 50)
        self.bulky_dimensions = (200, 200, 200)
        
    def test_standard_package(self):
        self.assertEqual(sort(*self.standard_dimensions, 5), "STANDARD")

    def test_bulky_package_volume(self):
        self.assertEqual(sort(*self.bulky_dimensions, 10), "SPECIAL")

    def test_bulky_package_dimension(self):
        self.assertEqual(sort(150, 50, 50, 10), "SPECIAL")

    def test_heavy_package(self):
        self.assertEqual(sort(*self.standard_dimensions, 25), "SPECIAL")

    def test_rejected_package(self):
        self.assertEqual(sort(*self.bulky_dimensions, 50), "REJECTED")

    def test_edge_cases(self):
        self.assertEqual(sort(1, 1, 1, 0.1), "STANDARD")  # Minimum values
        self.assertEqual(sort(149, 149, 149, 19), "STANDARD")  # Just under limits
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")  # At limits
        
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            sort(-1, 50, 50, 10)  # Negative dimension
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -5)  # Negative mass

    def test_decimal_values(self):
        self.assertEqual(sort(149.9, 149.9, 149.9, 19.9), "STANDARD")
        self.assertEqual(sort(150.1, 50, 50, 10), "SPECIAL")


if __name__ == "__main__":
    unittest.main()
