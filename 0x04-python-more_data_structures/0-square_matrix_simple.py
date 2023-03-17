#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []

    for element in matrix:
        result = list(map(lambda x: x**2, element))
    return result
