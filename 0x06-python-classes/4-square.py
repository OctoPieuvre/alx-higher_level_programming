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
        Returns:
            None
        """
        self.__size = size

    @property
    def size(self):
        """Getter of __size
        Returns:
            size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Settter of _size.
        Args:
            value (int): size of square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the square area.
        Returns:
            The area of the square
        """
        return (self.__size * self.__size)
