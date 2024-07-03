#!/usr/bin/python3
"""
Solution to lockbox problem
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    # A set to keep track of opened boxes
    opened = {0}
    # A list to keep track of keys to be processed
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key not in opened:
                opened.add(key)
                if key < len(boxes):
                    keys.append(key)

    return len(opened) == len(boxes)
