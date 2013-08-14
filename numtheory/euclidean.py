"""
Euclidean algorithms
"""

def gcd(a, b):
    """
    Computes gcd(a,b) by the Euclidean algorithm

    >>> gcd(6, 3)
    3

    >>> gcd(7, 13)
    1

    >>> gcd(4945257283, 3619535243)
    82651
    """

    while b != 0:
        a, b = b, a % b
    return a


def gcdex(a, b):
    """
    Computes gcd(a, b) by the extended Euclidean algorithm

    >>> gcdex(120, 25)
    (-1, 5, 5)

    >>> gcdex(4945257283, 3619535243)
    (11639, -15902, 82651)
    """

    x1, x0 = 0, 1
    y1, y0 = 1, 0

    while b != 0:
        q = a / b
        a, b = b, a % b
        x1, x0 = x0 - q*x1, x1
        y1, y0 = y0 - q*y1, y1
    return x0, y0, a
