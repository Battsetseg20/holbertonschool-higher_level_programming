#!/usr/bin/python3
"""Module containing the function that divides all elements of matrix"""


def matrix_divided(matrix, div):
    """divides elements matrix by the divisor div"""
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(x, list) for x in matrix) or
            not all((isinstance(n, int) or isinstance(n, float))
                    for n in [num for x in matrix for num in x])):
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = list(map(lambda x: list(map(lambda y: round(y/div, 2), x)), matrix))

    return (res)
