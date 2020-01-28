#!/usr/bin/python3
"""unittests for this project"""
import unittest
from models.rectangle import Rectangle
import sys
import io


class TestRectangle(unittest.TestCase):
    """Class with test cases for the Rectangle class"""

    def test_doc(self):
        """testing if doc exist"""
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)
        self.assertTrue(len(Rectangle.__str__.__doc__) > 0)
        self.assertTrue(len(Rectangle.width.__doc__) > 0)
        self.assertTrue(len(Rectangle.height.__doc__) > 0)
        self.assertTrue(len(Rectangle.x.__doc__) > 0)
        self.assertTrue(len(Rectangle.y.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)
        self.assertTrue(len(Rectangle.update.__doc__) > 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_id(self):
        """testing id counter and assignment"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r1.id, 6)
        self.assertAlmostEqual(r2.id, 7)
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

    def test_display(self):
        """test display"""
        tmp = sys.stdout
        sys.stdout = io.StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        res = "\n\n  ##\n  ##\n  ##\n"
        out = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = tmp
        self.assertAlmostEqual(out, res)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(height=1)
        res1 = str(r1)
        out = "[Rectangle] (10) 10/10 - 10/1"
        self.assertMultiLineEqual(res1, out)
