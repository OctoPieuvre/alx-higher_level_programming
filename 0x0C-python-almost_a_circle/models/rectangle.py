#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from models.base import Base


class Rectangle:
    """
        class Rectangle implements Base.
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class..
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter function for width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for width.
            Args:
                value (int): value to be set.
        """
        return self.__width = value

    @property
    def height(self):
        """
            getter function for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter fuction for height
            Args:
                value (int) value to be set.
        """
        return self.__height = value

    @property
    def x(self):
        """
            getter function for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x
            Args:
                Value (int) : value to be set
        """
        return self.__x = value

    @property
    def y(self):
        """
            getter function for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter for function y
            Args:
                Value (int) : value to be set
        """
        return self.__y = value
