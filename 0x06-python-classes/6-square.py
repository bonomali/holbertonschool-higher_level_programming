#!/usr/bin/python3
"""This is a module that defines a square class"""


class Square:
    """A class that defines a square.

    Attributes:
    size (int): the size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.
        Args:
        size (int): The size of the square
        position (tuple): the coordinates for the position of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """ Calculates the current area of the square
        Returns:
        The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the square in #'s to stdout
        """
        if self.__size is 0:
            print()
        else:
            a, b = self.__position
            for i in range(b):
                print()
            for j in range(self.__size):
                print(" " * a, end="")
                print ("#" * self.__size)

    @property
    def size(self):
        """Retrieves the size
        Returns:
        the size of the square
        """
        return self.__size

    @property
    def position(self):
        """ Find the position of the square
        Returns:
        the position
        """
        return self.__position

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

    @position.setter
    def position(self, value):
        """Sets the position of the square
        Args:
        value (int): the new position
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        a, b = value
        if type(a) is not int or type(b) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if a < 0 or b < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
