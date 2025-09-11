#!/usr/bin/python3
"""The function div all elements in matrix."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (int or float): the matrix
        div (int or float): divisor

    Returns:
        list: new matrix as result of the division
    """
    result = []
    for row in range(len(matrix)):
        if not isinstance(matrix[row], list):
            error_msg = (
                'matrix must be a matrix (list of lists) of integers/floats'
                )
            raise TypeError(error_msg)
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        new_row = []
        for col in range(len(matrix[row])):
            if not isinstance(matrix[row][col], (int, float)):
                raise TypeError(error_msg)
            elif div == 0:
                raise ZeroDivisionError('division by zero')
            elif not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            else:
                value = matrix[row][col] / div
                format_value = float('{:.2f}'.format(value))
            new_row.append(format_value)
        result.append(new_row)
    return result
