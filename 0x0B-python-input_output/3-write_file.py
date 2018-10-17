#!/usr/bin/python3
def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of chars written"""
    with open(filename, 'w') as file:
        return file.write(text)
