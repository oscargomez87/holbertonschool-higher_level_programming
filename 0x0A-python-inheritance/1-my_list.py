#!/usr/bin/python3
"""module for task 1"""


class MyList(list):
    """subclass of the list object"""
    def print_sorted(self):
        """sorts items of a list in ascending order"""
        new_list = eval(super().__repr__())
        new_list.sort()
        print(new_list)
