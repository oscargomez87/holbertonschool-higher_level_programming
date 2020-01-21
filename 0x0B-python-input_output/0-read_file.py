#!/usr/bin/python3
"""Module for task 0"""


def read_file(filename=""):
    """Opens a file in default mode"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
