#!/usr/bin/python3
"""
    this file include the solution of probelm 0x01. Lockboxes

    problem statement:
      You have n number of locked boxes in front of you.
      Each box is numbered sequentially from 0 to n - 1 and
      each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened.

    Args:
      boxes : is a list of lists

    Return:
      True if all boxes can be opened, else return False

    """
    if type(boxes) is not list:
        return False

    if len(boxes) == 0:
        return False

    visited = set([0])
    stack = [boxes[0]]

    while stack:
        boxes_to_visit = stack.pop()

        for box in boxes_to_visit:
            if box >= len(boxes):
                return False
            elif box not in visited:
                visited.add(box)
                stack.append(boxes[box])
    return True if len(boxes) == len(visited) else False
