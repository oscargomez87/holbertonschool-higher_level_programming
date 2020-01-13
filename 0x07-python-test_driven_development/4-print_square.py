#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """Prints a square useing "#"

    Args:
    size (int): size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        print("{}".format("#" * size), end="")
        print("")
