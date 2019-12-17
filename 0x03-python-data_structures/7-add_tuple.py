#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if not any(tuple_a):
        return tuple_b
    elif not any(tuple_b):
        return tuple_a
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0, )
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, )
    tuple_c = tuple(na + nb for na, nb in zip(tuple_a[:2], tuple_b[:2]))
    return tuple_c
