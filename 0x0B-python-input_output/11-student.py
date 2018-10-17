#!/usr/bin/python3
"""This is a module that contains a class Student"""

class Student:
    """Class that defines a student
    Attributes:
    first_name (str): the first name of the student
    last_name (str): the last name of the student
    age (int): the age of the student
    """
    def __init__(self, first_name, last_name, age):
        """Initialization of the student
        Args:
        first_name (str): the first name of the student
        last_name (str): the last name of the student
        age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
