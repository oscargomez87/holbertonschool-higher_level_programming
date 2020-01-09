#!/usr/bin/python3
"""This module defines a square class."""

class Square:
    """Defines a square of __size as size.
    Attributes:
    size (int): size of the square.
    """

    def __init__(self, size=0):
        """__init__ method for the Square class.

        If size is not an integer raises a TyperError, if size is
        less than 0 raises a ValueError, otherwise, assigns size to
        __size.

        Args:
        size (int): Size of the square
        """

        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        except TypeError:
                raise TypeError("size must be an integer")

    def area(self):
        """Defines the area of the square

        Returns:
        int: Area of the square
        """
        a = self.__size ** 2
        return a
