#!/usr/bin/python3
"""Define a function that prints my name"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first_name> <last_name> if last_name is not empty,
    and My name is <first_name> otherwise.

    :param first_name: A string representing the first name.
    :param last_name: A string representing the last name (optional, default
    is an empty string).
    :raises TypeError: If first_name is not a string or if last_name is not a
    string (if it is not empty).
    """


    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name})
