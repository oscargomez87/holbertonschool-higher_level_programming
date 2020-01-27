#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBase(unittest.TestCase):
    """Class with test cases for the Base class"""
    def test_id(self):
        """testing id counter and assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 10)
