#!/usr/bin/python3
"""This module defines a class Base"""

import json


class Base:
    """This class defines a Base
    Attributes:
    nb_objects (int): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of Base
        Args:
        id (int): the id number of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def dimension_validator(self, name, value):
        """Validates the given value
        Args:
        name (str): the name of the value
        value (int): the given value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def coord_validator(self, name, value):
        """Validates the given value
        Args:
        name (str): the name of the value
        value (int): the given value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries
        Args:
        list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_obj to a file
        Args:
        cls (class): the given class
        list_obj (list): a list of instances who inherits Base
        """
        string = []
        if list_objs is None:
            string = "[]"
            file.write(string)
        else:
            for i in list_objs:
                string.append(cls.to_dictionary(i))
            with open(cls.__name__ + ".json", 'w') as file:
                file.write(cls.to_json_string(string))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
        json_string (string): string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
        cls (class): the given class
        dictionary (dict): a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 2, 2, 2)
            dummy.update(**dictionary)
        if cls.__name__ == "Square":
            dummy = cls(2, 2, 2)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        Args:
        cls (class): the given class:
        """
        list = []
        try:
            with open(cls.__name__ + ".json", "r") as file:
                list = cls.from_json_string(file.read())
            for i in range(len(list)):
                list[i] = cls.create(**list[i])
        except FileNotFoundError:
            return ([])
        return (list)
