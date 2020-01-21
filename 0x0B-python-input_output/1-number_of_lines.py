#!/usr/bin/python3
"""Module for task 1"""


def number_of_lines(filename=""):
    """Returns the number of lines in a file"""
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
