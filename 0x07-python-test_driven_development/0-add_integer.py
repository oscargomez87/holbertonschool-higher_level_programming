#!/usr/bin/python3
"""Addition module"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args.
    a (int, float): first number to add
    b (int, float): second number to add
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
