#!/usr/bin/python3
def matrix_divided(matrix, div):
    """''def matrix_divided(matrix, div):'' divide each
    elelemt of the matrix is divided by div and
    return a new matrix with the results with a 2
    precision numbers. If div not is a number raise
    TypeError or ZeroDivisionError if div is 0:
    If matrix not is a list of lists return TypeError.
    If some sub-list aren't a list return TypeError.
    If some element of some sub-list aren't integer
    or float number return TypeError."""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of \
        integers/floats"
        )
    else:

        for i in matrix:
            if type(i) is not list:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
                integers/floats"
                )
            else:
                for j in i:
                    if type(j) not in [int, float]:
                        raise TypeError(
                            "matrix must be a matrix (list of lists) \
                        of integers/floats"
                        )

        r_len = len(matrix[0])
        for n in range(len(matrix)):
            if len(matrix[n]) != r_len:
                raise TypeError(
                    "Each row of the matrix must have \
                the same size"
                )

        New_matrix = [[round((el / div), 2) for el in i] for i in matrix]

    return New_matrix
