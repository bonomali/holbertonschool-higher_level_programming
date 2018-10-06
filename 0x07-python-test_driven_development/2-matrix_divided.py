#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all numbers in a matrix by a given number
    Args:
    matrix (list of lists): the given matrix
    div (int): the divisor
    """
    longerror = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(longerror)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(longerror)
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError(longerror)

    length = len(matrix[0])
    for k in matrix:
        if len(k) != length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div is not float):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by 0")

    new = []
    for i in range(len(matrix)):
        lis = []
        for j in range(len(matrix[i])):
            lis.append(round(matrix[i][j] / div, 2))
        new.append(lis)
    return new
