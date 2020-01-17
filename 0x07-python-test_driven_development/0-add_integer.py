#!/usr/bin/python3
"""This is  the "add_integer" module.
The add_interger module add a with b. For example,
>>> add_integer(1, 4)
5
"""


def add_integer(a, b=98):
    """This function sum a and b.
    Return the result int datatype.
    Raise TypeError if data is diferrent that int."""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, int) and isinstance(b, int):
        return int(a + b)
