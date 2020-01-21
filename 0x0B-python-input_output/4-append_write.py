#!/usr/bin/python3
"""Module for task 4"""


def append_write(filename="", text=""):
    """opens a file in append mode and inserts a text"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
