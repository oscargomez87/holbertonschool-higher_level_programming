#!/usr/bin/python3
"""Finds the peak number in a list"""


def find_peak(list_of_integers):
    if list_of_integers:
        list_of_integers.sort()
        idx = len(list_of_integers) - 1
        return list_of_integers[idx]
    else:
        return []
