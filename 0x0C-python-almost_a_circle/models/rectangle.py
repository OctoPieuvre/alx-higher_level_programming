#!/usr/bin/python3
"""contains class Rectangle which implements Base"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle implements Base.
        Methods:
            __init__()"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the instance of the class.
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the instnace rectangle"""
        return(self.__width * self.__height)

    def display(self):
        """prints to stdout the Rectangle instance with '#'"""

        rect = ""
        print_symb = "#"

        print("\n" * self.__y, end="")

        for i in range(self.__height):
            rect += (" " * self.__x) + (self.__width * print_symb) + "\n"
        print(rect, end="")

    def __str__(self):
        """return a string format"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """assigns key/value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args"""
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass
