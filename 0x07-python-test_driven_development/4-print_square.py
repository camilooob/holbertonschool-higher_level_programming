#!/usr/bin/python3
def print_square(size):
    """
    ''def print_square(size):'' Always is a entiger number.
    If the number is float, this number need be close and
    positive."""
    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) is float:
        size = int(size)
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
