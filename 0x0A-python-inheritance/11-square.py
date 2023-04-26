#!/usr/bin/python3
"""
Module for Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a Square object with provided size
        """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the Square object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
