#!/usr/bin/python3
"""this module contain rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """
    method to rotate matrix 90 degrees clockwise.
    Arguments:
      matrix : n x n matrix
    Return:
      None
    """

    for r in range(len(matrix)):
        for c in range(r, len(matrix[0])):
            if r == c:
                continue
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for row in matrix:
        row.reverse()
