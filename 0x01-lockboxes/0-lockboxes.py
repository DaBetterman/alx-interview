#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.
    """
    n = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == n
