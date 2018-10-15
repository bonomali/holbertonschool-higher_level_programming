#!/usr/bin/python3
def romvalue(char=''):
        romlib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'M': 1000}
        return romvalue[char]


def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""
    value = 
for letter in roman_string:
        if value(roman_string[letter + 1]) is None:
            total += value(letter)
        elif value(letter) >= value(letter + 1):
            total += value(letter)
        else:
            total -= value(letter)
    return total
