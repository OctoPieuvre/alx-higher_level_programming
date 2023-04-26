#!/usr/bin/python3
"""
Module for Rectangle class that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with provided width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the Rectangle object
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object
        """
        return "[{}] {}/{}".format(self.__class__.__name,self.__width, self.__height)

