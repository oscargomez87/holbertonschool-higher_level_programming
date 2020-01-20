#!/usr/bin/python3
"""Module for a class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize class attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """return a string representation of this class"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """returns the area of a Rectangle"""
        return (self.__width * self.__height)
