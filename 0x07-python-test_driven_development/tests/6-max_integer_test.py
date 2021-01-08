#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for 6-max_integer.py"""

    def test_list_integer(self):
        """Does list like [1, 2, 3, 4] work?"""
        max_int = max_integer([1, 2, 3, 4])
        self.assertEqual(max_int, 4)

    def test_list_unordered_ints(self):
        """Does list like [1, 2, 4, 3] work?"""
        max_int = max_integer([1, 2, 4, 3])
        self.assertEqual(max_int, 4)

    def test_max_at_begginning(self):
        """Does list with negative numbers work?"""
        max_int = [-4, -3, -2, -1]
        self.assertEqual(max_integer(max_int), -1)

    def test_empty_list(self):
        """Test an empty list."""
        max_int = []
        self.assertEqual(max_integer(max_int), None)

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_string(self):
        """Test a string."""
        string = "List"
        self.assertEqual(max_integer(string), 't')

    def test_floats(self):
        """Test a list of floats."""
        max_int = [1.5, 2.5, 3.5, 4.5]
        self.assertEqual(max_integer(max_int), 4.5)

    def test_int_in_list(self):
        """Test one int in a list"""
        ints_and_floats = [1.5, 2.5, 5, 3.5]
        self.assertEqual(max_integer(ints_and_floats), 5)







if __name__ == '__main__':
    unittest.main()
