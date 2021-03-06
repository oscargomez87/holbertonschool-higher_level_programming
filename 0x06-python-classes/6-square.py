#!/usr/bin/python3
"""This module defines a square class."""


class Square:
    """Defines a square of __size as size.
    Attributes:
    size (int): size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method for the Square class.
        Args:
        size (int): Size of the square.
        """
        self.size = size
        self.position = position

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
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square

        The setter method checks thevalue and if is not a tuple, has more
        or less than 2 elements, it's elements are not int and are negative

        Returns:
        tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(val) != int for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Defines the area of the square

        Returns:
        int: Area of the square
        """
        a = self.__size ** 2
        return a

    def my_print(self):
        """prints a square using the # char"""
        if self.__size == 0:
            print("")
            return
        for c in range(0, self.__position[1]):
            print("")
        for r in range(0, self.__size):
            for p in range(0, self.__position[0]):
                print(" ", end="")
            for c in range(0, self.__size):
                print("#", end="")
            print("")
