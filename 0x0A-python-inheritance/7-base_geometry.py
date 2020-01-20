#!/usr/bin/python3
"""Defines class BaseGeometry"""


class BaseGeometry:
    """Base geometry formulas"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value
        Args.
        name (str): name of the value
        value: variable that requires validation
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
