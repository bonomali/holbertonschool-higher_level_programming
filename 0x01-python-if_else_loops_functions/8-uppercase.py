#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase"""
    for l in str:
        upper = ord(l)
        if 97 <= upper <= 122:
            upper -= 32
        print('{}'.format(chr(upper)), end='')
    print()
