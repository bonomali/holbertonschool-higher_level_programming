#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    new = my_list[:]
    for i in my_list:
        if i % 2 is 0:
            new[i] = True
        else:
            new[i] = False
    return new
