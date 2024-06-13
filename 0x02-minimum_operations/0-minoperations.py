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


def minOperations(n: int) -> int:
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
    ans = [float("inf")]

    @cache
    def dfs(s: str, copy: str, num_operations: int) -> None:
        if len(s) == n:
            ans[0] = min(ans[0], num_operations)
            return

        if len(s) > n:
            return

        if copy != s:
            dfs(s, s, num_operations + 1)
        if copy:
            dfs(s + copy, copy, num_operations + 1)

    dfs("H", "", 0)
    return 0 if ans[0] == float("inf") else ans[0]
