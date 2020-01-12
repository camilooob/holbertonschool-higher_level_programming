"""This is  the "example" module.

The example module supplies one fuction, factorial(). For example,
Test 0:
>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    Test 1:
    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    Test 2:
    >>> factorial(30)
    265252859812191058636308480000000

    Test 3:
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Test 4 - Factorials of floats are OK, but the float must be an exact integer:
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    Test 5:
    >>> factorial(30.0)
    265252859812191058636308480000000

    Test 6 - It must also not be ridiculously large:
    >>> factorial(1e100)
    Traceback (most recent call last):
       ...
    OverflowError: n too large
    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n: #catch a vale like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    """
    Test 1:
    >>> add_integer(0, 0)
    0

    Test 2:
    >>> add_integer(0, -3)
    -3

    Test 3:
    >>> add_integer(-1, b)
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer

    Test 4:
    >>> add_integer(a, 5)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    Test 5:
    >>> add_integer(10.27564.10.5647335)
    20
    """
