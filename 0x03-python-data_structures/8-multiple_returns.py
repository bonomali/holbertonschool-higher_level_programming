#!/usr/bin/python3
def multiple_returns(sentence):
    """returns the length of a string and its first character"""
    if len(sentence) < 1:
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
