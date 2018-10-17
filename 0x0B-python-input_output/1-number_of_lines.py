#!/usr/bin/python3
def number_of_lines(filename=''):
    """Return the number of lines in a text file"""
    i = 0
    with open(filename) as file:
        for line in file:
            i += 1
    return(i)
