#!/usr/bin/python3
"""This is a module that defines a class BaseGeometry"""

class BaseGeometry:
	"""A class that defines BaseGeometry
	Attributes:
	area (int): not yet defined
	"""
	def area(self):
		"""Raises an exception"""
		raise Exception("area() is not implemented")

	def integer_validator(self, name, value):
		"""Validates the given value
		Args:
			name (str): the name of the value
			value (int): the given value
		"""
		if type(value) is not int:
			raise TypeError("{} must be an integer".format(name))
		if value <= 0:
			raise ValueError("{} must be greater than 0".format(name))
			
