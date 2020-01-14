#!/usr/bin/python3
"""This is  the "matrix_divided" function.
The matrix_divided function divided matrix. For example,
>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""
def matrix_divided(matrix, div):
    """This function divided a matrix.
    Return the result in new matrix.
    Raise Error if data is diferrent."""
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")
    else:

        for i in matrix:
            if type(i) is not list:
                raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
            else:
                for j in i:
                    if type(j) not in [int, float]:
                        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")

        lentrix = len(matrix[0])
        for n in range(len(matrix)):
            if len(matrix[n]) != lentrix:
                raise TypeError("Each row of the matrix must have \
                the same size")
    matrix1 = []
    matrix2 = []
    matrix10 = [matrix1, matrix2]
    z = 1
    for i in matrix:
        for j in i:
            if z <= 3:
                matrix1.append(float("{0:.2f}".format((j / div))))
            else:
                matrix2.append(float("{0:.2f}".format((j / div))))
            z += 1
    return matrix10
