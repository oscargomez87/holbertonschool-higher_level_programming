#!/usr/bin/python3
"""Model for rectangle class"""
from models.base import Base


class Rectangle(Base):
    """"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """returns a user friendly string representation of the rectangle"""
        return ("[Rectangle]" + "(" + str(self.id) + ") " + str(self.__x) +
                "/" + str(self.__y) + " - " + str(self.__width) +
                "/" + str(self.__height))

    @property
    def width(self):
        """getter/setter for attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter/setter for attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter/setter for attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter/setter for attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a representation of the rectangle using the character #"""
        print("{}".format("\n" * self.__y), end="")
        for row in range(self.__height):
            print("{}".format(" " * self.__x), end="")
            print("{}".format("#" * self.__width))

    def update(self, *args, **kwargs):
        """Updates the attributes of the class"""
        if args:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.__id = arg
                if idx == 1:
                    self.__width = arg
                if idx == 2:
                    self.__height = arg
                if idx == 3:
                    self.__x = arg
                if idx == 4:
                    self.__y = arg
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Return a dictionary representation of the class attributes"""
        new_dict = {'id': 0, 'width': 0, 'height': 0, 'x': 0, 'y': 0}
        for key in new_dict:
            new_dict[key] = getattr(self, key)
        return new_dict
