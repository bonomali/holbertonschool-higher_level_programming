#!/usr/bin/python3
def islower(c):
    """Checks for a lowercase character"""
    if 97 <= ord(c) <= 122:
        return True
    else:
        return False
