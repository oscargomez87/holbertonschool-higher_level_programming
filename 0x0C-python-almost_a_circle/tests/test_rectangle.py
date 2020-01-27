#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Class with test cases for the Rectangle class"""

    def test_id(self):
        """testing id counter and assignment"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r1.id, 5)
        self.assertAlmostEqual(r2.id, 6)
        self.assertAlmostEqual(r3.id, 12)

    def test_Type(self):
        """testing type of value in argument"""
        self.assertRaises(TypeError, Rectangle, (10, 2.5))
        self.assertRaises(TypeError, Rectangle, (10, "2"))
        self.assertRaises(TypeError, Rectangle, (10, []))
        self.assertRaises(TypeError, Rectangle, (10, {}))
        self.assertRaises(TypeError, Rectangle, (10, ()))
        self.assertRaises(TypeError, Rectangle, (10.3, 2))
        self.assertRaises(TypeError, Rectangle, ("10", 2))
        self.assertRaises(TypeError, Rectangle, ([], 2))
        self.assertRaises(TypeError, Rectangle, ({}, 2))
        self.assertRaises(TypeError, Rectangle, ((), 2))
        self.assertRaises(TypeError, Rectangle, (10, 2, 1.2))
        self.assertRaises(TypeError, Rectangle, (10, 2, "1"))
        self.assertRaises(TypeError, Rectangle, (10, 2, []))
        self.assertRaises(TypeError, Rectangle, (10, 2, {}))
        self.assertRaises(TypeError, Rectangle, (10, 2, ()))
        self.assertRaises(TypeError, Rectangle, (10, 2, 1, 10.1))
        self.assertRaises(TypeError, Rectangle, (10, 2, 1, "10"))
        self.assertRaises(TypeError, Rectangle, (10, 2, 1, []))
        self.assertRaises(TypeError, Rectangle, (10, 2, 1, {}))
        self.assertRaises(TypeError, Rectangle, (10, 2, 1, ()))

    def test_Value(self):
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.height = -2
            r.height = 0
            r.width = -1
            r.width = 0
            r.x = ""
            r.x = {}
            r.x = []
            r.x = ()
            r.x = 1.2
            r.y = ""
            r.y = {}
            r.y = []
            r.y = ()
            r.y = 1.2

    def test_area(self):
        """testing area of rectangle"""
        r = Rectangle(10, 2)
        self.assertAlmostEqual(r.area(), 20)
