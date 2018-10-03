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
        self.__size = size
