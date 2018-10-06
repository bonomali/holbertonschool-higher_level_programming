#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers.
    Args:
    a (int): first number
    b (int): second number
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
