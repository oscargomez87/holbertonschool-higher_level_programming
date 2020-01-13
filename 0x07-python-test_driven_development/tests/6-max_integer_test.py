#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test correct type of value
        self.assertAlmostEqual(max_integer([1, 2]), 2)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)
        self.assertAlmostEqual(max_integer("string"), "t")
        self.assertAlmostEqual(max_integer((1, 2)), 2)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 12)
        self.assertRaises(TypeError, max_integer, 2j)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(KeyError, max_integer, {'a' : 1, 'b' : 2})
