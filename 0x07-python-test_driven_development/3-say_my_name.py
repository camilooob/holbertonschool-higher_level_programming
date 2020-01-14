#!/usr/bin/python3
"""This is  the "matrix_divided" function.
The matrix_divided function divided matrix. For example,
>>> matrix_divided([[1, 2, 3],[4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""
def say_my_name(first_name, last_name=""):
    """This function divided a matrix.
    Return the result in new matrix.
    Raise Error if data is diferrent."""
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
