#!/usr/bin/python3
"""This module defines a class Rectangle
"""
class Rectangle:
    """A class that defines a rectangle
    Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """ Calculates the current area of the rectangle
        Returns:
        The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of the rectangle
        Returns:
        The perimeter of the rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)


    def __str__(self):
        """ Prints the rectangle
        Returns:
        the rectangle to stdout
        """
        if self.__width is 0 or self.__height is 0:
            return("")
        for i in range(self.__height - 1):
            print("#" * self.__width)
        return str("#" * self.__width)

    def __repr__(self):
        """Gives a string representation of the rectangle
        Returns:
        The rectangle info
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
    def __del__(self):
        """Deletes the rectangle and prints a message
        Returns:
        A farewell message
        """
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieves the width
        Returns:
        the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height
        Returns:
        the height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
        value (int): the new width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
        value (int): the new height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
