#!/usr/bin/python3
""" Function that count perimeter """


def island_perimeter(grid):
    """_summary_

    Args:
        grid (_type_): _description_
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):

            if grid[row][col] == 1:

                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1

                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1

                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1

                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
