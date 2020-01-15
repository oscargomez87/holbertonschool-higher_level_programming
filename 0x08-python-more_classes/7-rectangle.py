#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle:
    """Class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Attributes creation method

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string representation of a rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        text = ""
        for r in range(self.__height):
            text = text + "{}".format(str(self.print_symbol) * self.__width)
            if r < self.__height - 1:
                text = text + "\n"
        return text

    def __repr__(self):
        """Returns a string representation of the rectangle

        A new instance of this object can be created useing eval()
        on the return of this method.
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Cleans up resources used by the Rectangle class"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Defines the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def setPrint_symbol(value):
        """Sets the value of the symbol used to print the rectangle"""
        Rectangle.print_symbol = value

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Defines the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
