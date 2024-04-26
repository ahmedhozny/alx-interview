#!/usr/bin/python3
"""
A module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list containing the rows of Pascal's triangle.
    """
    if n < 1:
        return []

    if n == 1:
        return [[1]]

    triangle = [[1], [1, 1]]

    if n == 2:
        return triangle

    for i in range(2, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        row.append(1)
        triangle.append(row)

    return triangle
