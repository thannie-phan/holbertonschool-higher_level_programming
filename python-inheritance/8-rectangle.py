#!/usr/bin/python3
"""This module defines class base geometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This defines class Rectangle. """

    def __init__(self, width, height):
        """This defines the rectangle."""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
