#!/usr/bin/python3
"""Matrix div module"""


def matrix_divided(matrix, div):
    """Divides the elements in a matrix

    Args:
    matrix (int matrix): elements to divide
    div (int): number to divide matrix elements with

    Returns:
    new_list: a new list with the result of the div
    """
    new_list = []
    notList = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or all(type(lt) != list for lt in matrix):
        raise TypeError(notList)
    for lt in matrix:
        if not all(type(val) in [int, float] for val in lt):
            raise TypeError(notList)
    if not all(len(lt) == len(matrix[0]) for lt in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for lt in matrix:
        new_list.append([round(val / div, 2) for val in lt])
    return new_list
