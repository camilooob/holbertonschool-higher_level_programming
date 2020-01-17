#!/usr/bin/python3
def add_integer(a, b=98):
    """
    This function sum a and b.
    Return the result int datatype.
    Raise TypeError if data is diferrent that int.
    """
    if type(a) in [int, float]:
        num1 = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) in [int, float]:
        num2 = int(b)
    else:
        raise TypeError("b must be an integer")

    if type(num1) is int and type(num2) is int:
        return num1 + num2
