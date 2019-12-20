#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        squares = list(map(lambda x: x**2, i))
        new.append(squares)
    return new
