#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """This class is for make unit testi"""

    def number_test(self):
        """This function make unit test for the funtion
        max_integer"""
        self.assertAlmostEqual(max_integer([10, 5, 7, -3]), 10)
        self.assertAlmostEqual(max_integer([1, 1.5, 2, 2.5]), 2.5)
        self.assertAlmostEqual(max_integer([-1, -2, -3, 0]), 0)
        self.assertAlmostEqual(max_integer([]), None)

    def raised_text(self):
        """This function identify the raised errors"""
        self.assertAlmostEqual(max_integer({5, 0}), 5)
        self.assertRaises(TypeError, max_integer, "hola")
        self.assertRaises(TypeError, max_integer, [5j, 1, 7])
        self.assertRaises(TypeError, max_integer, [5e123456, 7, 9])
