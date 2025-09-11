#!/usr/bin/python3
"""The function print a square using #"""


def print_square(size):
    """
    Print a square using #

    Args:
        size: size of the square

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size > 0:
        size = int(size)
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print("")
