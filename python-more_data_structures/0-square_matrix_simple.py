#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row.copy() for row in matrix]
    for row in range(len(new_matrix)):
        for col in range(len(new_matrix[row])):
            new_matrix[row][col] **= 2       
    return new_matrix
# End of function
