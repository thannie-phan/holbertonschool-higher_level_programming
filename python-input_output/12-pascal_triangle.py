#!/usr/bin/python3
"""This module defines class student."""


def pascal_triangle(n):
    """This returns list of int rep the triangle of n."""
    if n <= 0:
        return []

    pascals_triangle = []

    for row_number in range(n):
        row_numbers = [1]

        above_row_number = row_number - 1
        if above_row_number >= 0:
            row_above = pascals_triangle[above_row_number]

            for position_in_row_numbers in range(1, row_number):
                number_to_add = row_above[position_in_row_numbers - 1] + row_above[position_in_row_numbers]
                row_numbers.append(number_to_add)

            row_numbers.append(1)

        pascals_triangle.append(row_numbers)

    return pascals_triangle
