#!/usr/bin/python3
"""
    this file include the solution of probelm 0x00. Pascal's Triangle

    problem statement:
      return pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal's triangle of n

    Args:
      n : integer represent number of rows

    Return:
      list of lists expresses pascal triangle

    """
    triangle = [[1] * i for i in range(1, n + 1)]

    for i in range(2, n):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

    return triangle
