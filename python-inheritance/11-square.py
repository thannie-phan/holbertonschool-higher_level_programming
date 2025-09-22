#!/usr/bin/python3
"""This module defines class square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This defines class Square. """

    def __init__(self, size):
        """This defines the size of square."""

        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """This returns the area of square"""
        return super().area()

    def __str__(self):
        """This returns the print() and str()
        representation of the square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
