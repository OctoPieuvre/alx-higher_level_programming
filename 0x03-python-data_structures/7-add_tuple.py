#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l_a = len(tuple_a)
    l_b = len(tuple_b)
    if l_a < 1:
        tuple_a = (0, 0)
    elif l_a < 2:
        tuple_a = (tuple_a[0], 0)

    if l_b < 1:
        tuple_b = (0, 0)
    elif l_b < 2:
        tuple_b = (tuple_b[0], 0)

    tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_c
