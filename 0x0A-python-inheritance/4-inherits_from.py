#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """
    Returns True if `obj` is an instance of a class that
    inherited (directly or indirectly) from `a_class`, otherwise False.

    Args:
    obj: The object to test.
    a_class: The class to compare against.

    Returns:
    True if `obj` is an instance of a class that inherited
    (directly or indirectly) from `a_class`, otherwise False.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
