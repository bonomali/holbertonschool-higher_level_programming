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
