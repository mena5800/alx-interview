#!/usr/bin/python3
"""this module contains island_perimeter"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    rows = len(grid)
    cols = len(grid[0])
    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                continue
            connections = 4
            for dx, dy in dirs:
                new_row = r + dx
                new_col = c + dy
                if new_row >= 0 and new_row < rows and \
                    new_col >= 0 and new_col < cols and \
                        grid[new_row][new_col]:
                    connections -= 1

            ans += connections

    return ans
