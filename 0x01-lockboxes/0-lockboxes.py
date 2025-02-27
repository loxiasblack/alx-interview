#!/usr/bin/python3
""" LockBoxes"""


def canUnlockAll(boxes):
    """
        retuen if all boxes opened
    """
    keys = {0}
    opened = set()
    n_boxes = len(boxes)

    while (keys - opened):
        current = (keys - opened).pop()
        opened.add(current)
        for key in boxes[current]:
            if key not in opened and key < n_boxes:
                keys.add(key)
    return (len(opened) == n_boxes)
