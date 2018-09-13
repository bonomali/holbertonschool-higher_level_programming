#!/usr/bin/python3
def remove_char_at(str, n):
    """removes the nth letter from a string"""
    if n >= 0:
        return(str[0:n] + str[n + 1:])
    else:
        return str
