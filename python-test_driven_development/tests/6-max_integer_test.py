#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list with the max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5, 3.5]), 3.5)

    def test_mixed_integers_and_floats(self):
        """Test a list of mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_negative_integers(self):
        """Test a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -0.5]), -0.5)

    def test_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_empty_string_in_list(self):
        """Test a list with an empty string"""
        self.assertEqual(max_integer(["", "a", "ab"]), "ab")


if __name__ == '__main__':
    unittest.main()