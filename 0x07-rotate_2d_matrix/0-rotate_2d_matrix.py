#!/usr/bin/python3
""" module for rotate 2d matrix n n"""


def rotate_2d_matrix(matrix):
    """Rotate the given n x n 2D matrix 90 degrees clockwise."""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
