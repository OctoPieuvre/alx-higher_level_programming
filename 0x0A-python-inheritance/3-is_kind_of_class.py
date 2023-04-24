#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if `obj` is an instance of `a_class`
    or any of its subclasses, otherwise False.

    Args:
    obj: The object to test.
    a_class: The class to compare against.

    Returns:
    True if `obj` is an instance of `a_class`
    or any of its subclasses, otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
