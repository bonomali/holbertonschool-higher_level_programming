#!/usr/bin/python3
def inherits_from(obj, a_class):
	"""Determines if the object is an instance of a class that inerited from a specified class
	"""
	if type(obj) == a_class:
		return False
	return issubclass(type(obj), a_class)
