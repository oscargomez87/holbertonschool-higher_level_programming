#!/usr/bin/python3
"""This module defines a square class."""

class Square():
    """Defines a square of __size size.
    Attributes:
    size : size of square
    """

    def __init__(self, size):
        """__init__ method for the Square class.

        Defines the attributes of the class Square.

        Args:
        size (int): Size of the square
        """
        self.__size = size
