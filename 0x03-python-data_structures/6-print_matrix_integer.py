#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    if matrix[0] is not None:
        for i in matrix:
            for j in i:
                if j is not i[len(i) - 1]:
                    print("{} ".format(j), end="")
                else:
                    print ("{}".format(j), end="")
            print()
