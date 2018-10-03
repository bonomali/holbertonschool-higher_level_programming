#!/usr/bin/python3
"""This is a module that defines a square class"""


class Square:
    """A class that defines a square.

    Attributes:
    size (int): the size of the square
    """
    def __init__(self, size=0):
        """Initializes the square.
        Args:
        size (int): The size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Calculates the current area of the square
        Returns:
        The area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Retrieves the size
        Returns:
        the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
        value (int): the new size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
