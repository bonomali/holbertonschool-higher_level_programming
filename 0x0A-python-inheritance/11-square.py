#!/usr/bin/python3
"""This is a module that defines a class Square"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
	"""A class that defines a square
	Attributes:
		size (int): the size of the square
	"""
	def __init__(self, size):
		"""Initializes the square
		Args:
			size (int): the size of the square
		"""
		self.integer_validator("size", size)
		self.__size = size
		super().__init__(size, size)

	def __str__(self):
		""" Prints the Square
		Returns:
		the square to stdout
		"""
		return ("[Square] {}/{}".format(self.__size, self.__size))
