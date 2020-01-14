#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class for unit test"""

    def number_test(self):
        """This function make unit to max_integer"""
        self.assertAlmostEqual(max_integer([12, 2, 4, -5]), 12)
        self.assertAlmostEqual(max_integer([3, 2.5, 5, 3.5]), 4.5)
        self.assertAlmostEqual(max_integer([-2, -3, -5, 0]), 0)
        self.assertAlmostEqual(max_integer([]), None)

    def raised_test(self):
        """This function raised error"""
        self.assertAlmostEqual(max_integer({3, 0}), 6)
        self.assertRaises(TypeError, max_integer, "hiii")
        self.assertRaises(TypeError, max_integer, [7j, 3, 4])
        self.assertRaises(TypeError, max_integer, [4e123356, 1, 3])
