#!/usr/bin/python
import json

def class_to_json(obj):
    """Returns the dictionary desciptions with simple data
    structure for JSON serialization of an object"""
    return obj.__dict__