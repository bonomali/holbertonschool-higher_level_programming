#!/usr/bin/python3
def lookup(obj):
    """Returns a list of available attributes and methods of an object
    Args:
        obj (object): the given object
    Returns:
        a list of available attributes and methods
    """
    return dir(obj)
