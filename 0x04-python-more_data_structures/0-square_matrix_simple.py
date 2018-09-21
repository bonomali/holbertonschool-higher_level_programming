#!/usr/bin/bash/python3
def square_matrix_simple(matrix=[]):
    """computes the square of all values in a matrix"""
    return [[item ** 2 for item in row] for row in matrix]
