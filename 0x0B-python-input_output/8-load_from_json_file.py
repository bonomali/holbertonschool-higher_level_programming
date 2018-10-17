#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename) as file:
        return json.loads(file.read())
