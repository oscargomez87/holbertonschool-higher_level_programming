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
            text = text + "{}".format(self.print_symbol * self.__width)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """checks the bigger rectangle

        If rect_1 is equal or bigger than rect_2 returns rect_1
        otherwise returns rect_2

        Args:
        rect_1 (Rectangle): Rectangle for comparison
        rect_2 (Rectangle): Rectangle for comparison
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a rectangle instance"""
        return cls(size, size)
