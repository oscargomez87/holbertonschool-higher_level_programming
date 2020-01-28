#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    """Class with test cases for the Base class"""
    def test_doc(self):
        """Testing if doc exist """
        self.assertTrue(len(Square.__doc__) > 0)
