#!/usr/bin/python3
"""This is  the "matrix_divided" function.
The matrix_divided function divided matrix. For example,
>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""
def matrix_divided(matrix, div):
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
