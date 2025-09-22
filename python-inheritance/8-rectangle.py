#!/usr/bin/python3
"""This module defines class base geometry."""


class BaseGeometry:
    """This defines class base geometry. """

    def area(self):
        """Raises an Exception with the message area() is
        not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This defines class Rectangle. """

    def __init__(self, width, height):
        """This defines the rectangle."""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
