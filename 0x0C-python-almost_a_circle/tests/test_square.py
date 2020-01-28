#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    """Class with test cases for the Base class"""
    def test_doc(self):
        """Testing if doc exist """
        self.assertTrue(len(Square.__doc__) > 0)

    def test_id(self):
        """testing id counter and assignment"""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        s3 = Square(10, 0, 0, 12)
        self.assertAlmostEqual(s1.id, 8)
        self.assertAlmostEqual(s2.id, 9)
        self.assertAlmostEqual(s3.id, 12)
