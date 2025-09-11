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
    for row in range (len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[row]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for col in range(len(matrix[row])):
            if not isinstance(matrix[row][col], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            try:
                value = matrix[row][col] / div
                format_value = float('{:.2f}'.format(value))
            except div == 0:
                ZeroDivisionError('division by zero')
            except not isinstance(div, (int, float)):
                TypeError("div must be a number")
            finally:
                result.append(format_value)
    return result