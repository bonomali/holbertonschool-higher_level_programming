#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """Reads n lines of a file and prints it to stdout"""

    i = 0
    with open(filename) as file:
        for line in file:
            i += 1
            print(line, end="")
            if nb_lines == i:
                break
