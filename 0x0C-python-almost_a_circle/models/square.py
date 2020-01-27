#!/usr/bin/python3
"""Model for a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that define a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialize attributes for Rectangle"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints a user friendly string representation of a square"""
        return ("[Square] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """getter/setter for attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update class attributes"""
        if args:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                if idx == 1:
                    self.size = arg
                if idx == 2:
                    self.x = arg
                if idx == 3:
                    self.y = arg
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """Return a dictionary representation of the class attributes"""
        new_dict = {'id': 0, 'size': 0, 'x': 0, 'y': 0}
        for key in new_dict:
            new_dict[key] = getattr(self, key)
        return new_dict
