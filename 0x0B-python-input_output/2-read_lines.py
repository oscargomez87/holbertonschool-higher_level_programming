#!/usr/bin/python3
"""Module for task 2"""


def read_lines(filename="", nb_lines=0):
    """Opens a file and reads n number of lines"""
    with open(filename, encoding='utf-8') as f:
        line_length = len(f.readlines())
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= line_length:
            print(f.read(), end='')
        else:
            for num, line in enumerate(f):
                if num < nb_lines:
                    print(line, end='')
