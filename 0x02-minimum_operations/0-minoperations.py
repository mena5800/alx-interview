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
from functools import cache


def minOperations(n):
    """
    method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.

    Args:
      n : int

    Return:
      num If n is impossible to achieve, return 0

    """

    if n == 1:
        return 0

    def dfs(cur, last_copy, n_operations):
        if cur == n:
            return n_operations

        if cur > n:
            return float("inf")

        return min(dfs(cur * 2, cur, n_operations + 2),
                   dfs(cur + last_copy, last_copy, n_operations + 1))

    ans = dfs(2, 1, 2)
    return 0 if ans == float("inf") else ans
