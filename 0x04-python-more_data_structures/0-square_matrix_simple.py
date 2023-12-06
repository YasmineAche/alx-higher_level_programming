#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = map(lambda x: x * x, row)
        new_matrix.append(list(new_row))
    return new_matrix
