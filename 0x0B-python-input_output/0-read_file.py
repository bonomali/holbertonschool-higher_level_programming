#!/usr/bin/python3
def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename) as file:
        for line in file:
            print(line, end="")
