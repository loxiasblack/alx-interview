#!/usr/bin/python3
""" function that returns the perimeter of the island described in grid """


def island_perimeter(grid):
    # grid is a list of lists of integers

    perimeter = 0
    # iterate through the grid
    for i in range(len(grid)):
        # iterate through the sublists
        for j in range(len(grid[i])):

            # if the current cell is a land cell
            if grid[i][j] == 1:

                # add 4 to the perimeter
                perimeter += 4

                # if the cell above is a land cell,
                # subtract 2 from the perimeter
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # if the cell to the left is a land cell,
                # subtract 2 from the perimeter
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
