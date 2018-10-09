#!/usr/bin/python3
"""This module defines a class Rectangle
"""

class Rectangle:
    """A class that defines a rectangle
    Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle.
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            print(str(self.print_symbol) * self.__width)
        return str(str(self.print_symbol) * self.__width)

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
        Rectangle.number_of_instances -= 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle
        Args:
        rect_1 (int): the first rectangle
        rect_2 (int): the second rectangle
        Returns:
        the bigger rectangle, or rect_1 if they are the same
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle that is, in fact, a square
        Args:
        size (int): the size of the square
        Returns:
        The new Rectangle
        """
        cls.number_of_instances += 1
        return Rectangle(size, size)
