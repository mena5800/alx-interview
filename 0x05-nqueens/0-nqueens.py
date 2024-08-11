#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem."""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

n = 0
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

cols = set()
posDig = set()
negDig = set()

grid = [["." for col in range(n)] for row in range(n)]
final_ans = []


def backtrack(r):
    """this function to get all possible ways of n not attacking queens."""
    if r == n:
        ans = []
        for row in range(n):
            for col in range(n):
                if grid[row][col] == "Q":
                    ans.append([row, col])
        final_ans.append(ans)
        return

    for c in range(n):
        if c in cols or (r + c) in posDig or (r - c) in negDig:
            continue

        cols.add(c)
        posDig.add(r + c)
        negDig.add(r - c)
        grid[r][c] = "Q"

        backtrack(r + 1)

        cols.remove(c)
        posDig.remove(r + c)
        negDig.remove(r - c)
        grid[r][c] = "."


backtrack(0)
for row in final_ans:
    print(row)
