#!/usr/bin/python3
"""This is a module that defines a class list"""

class MyList(list):
	"""A class that defines MyList"""
	def print_sorted(self):
		"""Prints a sorted list"""
		print(sorted(self))
