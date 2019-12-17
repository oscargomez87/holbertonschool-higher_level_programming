#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    tuple_c = tuple(na + nb for na, nb in zip(tuple_a[:2], tuple_b[:2]))
    return tuple_c
