#!/usr/bin/python3
"""This module defines class rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This defines class Rectangle. """

    def __init__(self, width, height):
        """This defines the rectangle."""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This returns the print() and str()
        representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
