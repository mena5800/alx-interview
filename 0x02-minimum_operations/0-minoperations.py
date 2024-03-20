#!/usr/bin/python3
"""
    this file include the solution of probelm 0x01. Lockboxes

    problem statement:
      You have n number of locked boxes in front of you.
      Each box is numbered sequentially from 0 to n - 1 and
      each box may contain keys to the other boxes.
"""
from functools import cache


def minOperations(n):
    """
    method that determines if all the boxes can be opened.

    Args:
      boxes : is a list of lists

    Return:
      True if all boxes can be opened, else return False

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
