#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list of single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test a list of multiple elements"""
        self.assertEqual(max_integer([1, 5, 3, 7, 2]), 7)

    def test_duplicate_elements(self):
        """Test a list of duplicate elements"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_positive_elements_end(self):
        """Test a list with max element at end"""
        self.assertEqual(max_integer([1, 35, 12, 7, 50]), 50)

    def test_positive_elements_middle(self):
        """Test a list with max element at middle"""
        self.assertEqual(max_integer([1, 35, 50, 7, 12]), 50)

    def test_positive_elements_beginning(self):
        """Test a list with max element at beginning"""
        self.assertEqual(max_integer([50, 1, 12, 7, 35]), 50)

    def test_all_negative_elements(self):
        """Test a list of negative elements"""
        self.assertEqual(max_integer([-1, -5, -3, -7, -2]), -1)

    def test_one_negative_elements(self):
        """Test a list of one negative element"""
        self.assertEqual(max_integer([1, 5, -3, 7, 2]), 7)

    def test_float_elements(self):
        """Test a list of float elements"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_elements(self):
        """Test a list of mixed elements"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_string_elements(self):
        """Test of a string"""
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

if __name__ == "__main__":
    unittest.main()
