#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = [[a ** 2 for a in row] for row in matrix]
    return n_matrix
