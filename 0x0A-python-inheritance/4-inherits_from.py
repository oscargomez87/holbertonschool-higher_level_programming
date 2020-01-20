#!/usr/bin/python3
"""module for task 4"""


def inherits_from(obj, a_class):
    """checks if obj is of the same class or inherits from a_class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
