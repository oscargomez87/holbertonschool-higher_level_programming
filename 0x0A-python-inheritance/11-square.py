#!/usr/bin/python3
"""Module for a class that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from BaseGeometry"""

    def __init__(self, size):
        """initialize class attributes"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """returns the area of a square"""
        return (self.__size ** 2)
