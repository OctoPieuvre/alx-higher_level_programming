#!/usr/bin/python3
"""A class that defines a square by size and position"""

class Square:
    """A class that defines a square by size and position
    Attributes:
        size (int): size of square.
    """

    def __init__(self, size=0, position=(0,0)):
        """Initializes a new square.
        Args:
            size (int): the size of square.
        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter of __position
        Returns:
            position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if type(value)is not tuple or len(value) != 2 or type(value[0]) is not int or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculate the square area.
        Returns:
            The area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ Print square with #.
        Returns:
            ###
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
