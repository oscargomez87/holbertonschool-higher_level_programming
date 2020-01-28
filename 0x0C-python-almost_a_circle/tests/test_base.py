#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBase(unittest.TestCase):
    """Class with test cases for the Base class"""

    def test_doc(self):
        """Testing if doc exist """
        self.assertTrue(len(Base.__doc__) > 0)
        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)
        self.assertTrue(len(Base.__init__.__doc__) > 0)

    def test_id(self):
        """testing id counter and assignment"""
        b1 = Base()
        b2 = Base()
        b3 = Base(10)
        self.assertAlmostEqual(b1.id, 1)
        self.assertAlmostEqual(b2.id, 2)
        self.assertAlmostEqual(b3.id, 10)
