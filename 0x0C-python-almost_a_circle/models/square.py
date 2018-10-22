#!/usr/bin/python3
"""This is a module that defines a class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that defines a square
    Attributes:
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square
        Args:
        size (int): the size of the square
        x (int): the x coord
        y (int): the y coord
        id (int): the id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the info on the square
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.width))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args:
            attr = ['id', 'size', 'x', 'y']
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square
        """
        return {'id': self.id, 'size': self.height, 'x': self.x, 'y': self.y}

    @property
    def size(self):
        """Retrieves the size
        Returns:
        the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square
        Args:
        value (int): the new size of the square
        """
        self.width = value
        self.height = value
