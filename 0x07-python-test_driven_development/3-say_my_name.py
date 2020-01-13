#!/usr/bin/python3
"""This module prints a message"""


def say_my_name(first_name, last_name=""):
    """Prints the message "My name is <first name> <last name>"

    Args:
    first_name (string): string to use in message
    last_name (string): string to use in message
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
