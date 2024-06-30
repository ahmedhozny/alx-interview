#!/usr/bin/python3
""" Island Perimeter calculation module
"""


def island_perimeter(grid):
    """
    Main function that calculates the island perimeter by taking grid
    (a list of lists of integers) as input and returns an integer indicating
    the perimeter of the island.
    """

    perimeter = 0
    m, n = len(grid), len(grid[0])
    for row in range(m):
        for col in range(n):
            if grid[row][col] == 0:
                continue

            x = 4
            if row - 1 >= 0 and grid[row - 1][col] == 1:
                x -= 1
            if row + 1 < m and grid[row + 1][col] == 1:
                x -= 1
            if col - 1 >= 0 and grid[row][col - 1] == 1:
                x -= 1
            if col + 1 < n and grid[row][col + 1] == 1:
                x -= 1

            perimeter += x

    return perimeter
