#!/usr/bin/python3
"""This is a module that defines a class rectangle"""

from models.base import Base


class Rectangle(Base):
    """A class that defines a rectangle
    Attributes:
    width (int): the width of the rectangle
    height (int): the height of the rectangle
    x (int): the x coordinate
    y (int): the y coordinate
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle
        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        x (int): the x coordinate
        y (int): the y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """ Calculates the current area of the rectangle
        Returns:
        The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle
        Returns:
        the rectangle to stdout
        """
        if self.__width is 0 or self.__height is 0:
            return("")
        else:
            for i in range(self.__y):
                print()
            for j in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

    def __str__(self):
        """Returns the rectangle id, coords, and size
        """
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                   self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args:
            attr = ['id', 'width', 'height', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

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

    @property
    def x(self):
        """Retrieves the x coord
        Returns:
        the x coord of the rectangle
        """
        return self.__x

    @property
    def y(self):
        """Retrieves the y coord
        Returns:
        the y coord of the rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
        value (int): the new width of the rectangle
        """
        self.dimension_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
        value (int): the new height of the rectangle
        """
        self.dimension_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x coord of the rectangle
        Args:
        value (int): the new x coord of the rectangle
        """
        self.coord_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y coord of the rectangle
        Args:
        value (int): the new y coord of the rectangle
        """
        self.coord_validator("y", value)
        self.__y = value
