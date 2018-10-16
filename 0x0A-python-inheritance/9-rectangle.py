#!/usr/bin/python3
"""This is a module that defines a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines a rectangle
    Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
    """
    def __init__(self, width, height):
        """Initializes the rectangle
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Calculates the current area of the rectangle
        Returns:
        The area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """ Prints the rectangle
        Returns:
        the rectangle to stdout
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
