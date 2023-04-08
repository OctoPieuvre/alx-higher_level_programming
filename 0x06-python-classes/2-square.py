#!/usr/bin/python3

""" Define a class Square. """

class Square:
    """Represent a square.

    Attributes:
        size (int): size of square.
    """

    def __init__(self, size=0):
        """Initializes a new square.

            Args:
                size (int): the size of square.
            Raises:
                TypeError: if size is not an integer.
                ValueError: if size is < 0.
                
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
