#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        return dict(zip(list(a_dictionary.keys()),
                        list(map(lambda x: x*2, a_dictionary.values()))))
