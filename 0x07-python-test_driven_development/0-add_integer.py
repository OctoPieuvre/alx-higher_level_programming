#!/usr/bin/python3
"""a function yhat add two integer"""


def add_integer(a, b=98):
    """"Returns an integer: the addition of a and b

    a and b must be first casted to integers if they are float

    Raises:
        TypeError: if a and b are not int or float

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
