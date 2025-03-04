#!/usr/bin/python3
"""function"""


def pascal_triangle(n):
    """
    define the function
    """
    pascal = []
    for i in range(n+1):
        row = [pascal[i - 1][y - 1] + pascal[i - 1][y]
               if (y < i - 1 and y != 0) else 1 for y in range(i)]
        pascal.append(row)
    pascal.pop(0)
    return pascal
