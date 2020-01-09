#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """Defines a square of __size as size.
    Attributes:
    size (int): size of the square.
    """

    def __init__(self, size=0):
        """__init__ method for the Square class.
        Args:
        size (int): Size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        The setter method checks the value and if is not an integer raises
        a TyperError, if size is less than 0 raises a ValueError.

        Returns:
        int: size of square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("size must be >= 0")
        if type(value) != int:
            raise TypeError("size must be an integer")
        self.__size = value

    def area(self):
        """Defines the area of the square

        Returns:
        int: Area of the square
        """
        a = self.__size ** 2
        return a
