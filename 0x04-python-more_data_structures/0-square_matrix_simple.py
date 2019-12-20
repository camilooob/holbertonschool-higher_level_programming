#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = []
    for i in matrix:
        squares = list(map(lambda x: x**2, i))
        a.append(squares)
    return a
