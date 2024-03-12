#!/usr/bin/python3

def canUnlockAll(boxes):
    visited = set([0])
    queue = [boxes[0]]

    while queue:
        boxes_to_visit = queue.pop(0)

        for box in boxes_to_visit:
            if box not in visited:
                visited.add(box)
                queue.append(boxes[box])

    return True if len(boxes) == len(visited) else False
