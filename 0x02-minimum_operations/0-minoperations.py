#!/usr/bin/python3

"""
    this file include the solution of probelm 0. Minimum Operations

    problem statement:
      In a text file, there is a single character H.
      Your text editor can execute only two operations
      in this file: Copy All and Paste. Given a number n,
      write a method that calculates the fewest number of
      operations needed to result in exactly n H characters
      in the file.
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
      n : int

    Return:
      num If n is impossible to achieve, return 0

    """
    if type(n) != int or n < 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
