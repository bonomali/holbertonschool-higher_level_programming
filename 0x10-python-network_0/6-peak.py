#!/usr/bin/python3
def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers
    Attributes:
        list_of_integers (list): given list to find peak in
    Returns:
        the integer that is the peak
    """
    if list_of_integers is None:
        return None
    elif len(list_of_integers) is 1:
        return list_of_integers[0]
    else
        return max(list_of_integers)
