#!/usr/bin/python3
"""Module for task 14"""


def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle"""
    l1 = []
    for i in range(n):
        l1.append([])
        l1[i].append(1)
        if i > 0:
            for e in range(i - 1):
                l1[i].append(l1[i - 1][e] + l1[i][e])
            l1[i].append(1)
    return l1
