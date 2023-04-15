#!/usr/bin/python3
"""Define a function printing a square."""


def print_square(size):
    """
    Prints a square with the character #.
    Args:
        size: the size length of the square
    Raise:
        TypeError: if size is not an integer
        TypeError: if size is float and is less than o
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
