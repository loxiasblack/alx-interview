#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Create a function that returns a list of lists
    of integers representing the Pascal’s triangle
    """
    trl = []

    if n > 0:
        for i in range(n):
            # Initialize the row with all 1s
            row = [1] * (i + 1)

            for j in range(1, i):
                a = trl[i - 1][j]
                b = trl[i - 1][j - 1]
                row[j] = a + b

            trl.append(row)

    return trl
