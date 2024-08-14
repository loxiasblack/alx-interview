#!/usr/bin/python3
""" module for rotate 2d matrix n n"""


def rotate_2d_matrix(matrix):
    """new method that rotate 2d matrix"""
    rotate_2d_matrix = []

    j = 0

    while j < len(matrix):
        i = len(matrix) - 1
        line = []
        while i >= 0:
            line.append(matrix[i][j])
            i = i - 1
        rotate_2d_matrix.append(line)
        j += 1
    n = 0
    x = len(matrix)
    while n < x - 1:
        matrix.pop(n)
        matrix.append(rotate_2d_matrix[n])
        n += 1
    matrix.pop(0)
    matrix.append(rotate_2d_matrix[-1])
    return matrix
