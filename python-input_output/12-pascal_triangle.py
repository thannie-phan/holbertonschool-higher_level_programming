#!/usr/bin/python3
"""This module defines class student."""


def pascal_triangle(n):
    """This returns list of int rep the triangle of n."""
    if n <= 0:
        return []

    triangle = []
    for current_row_index in range(n):
        current_row = [1]

        previous_row_index = current_row_index - 1
        if previous_row_index >= 0:
            previous_row = triangle[previous_row_index]

            for position_in_row in range(1, current_row_index):
                value = (
                    previous_row[position_in_row - 1]
                    + previous_row[position_in_row]
                )
                current_row.append(value)

            current_row.append(1)

        triangle.append(current_row)

    return triangle
