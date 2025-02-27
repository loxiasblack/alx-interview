#!/usr/bin/python3
""" LockBoxes"""


def canUnlockAll(boxes):
    """
        retuen if all boxes opened
    """
    keys = {0}
    opened = set()
    
    while keys - opened:
        current = (keys - opened).pop()
        opened.add(current)
        
        for key in boxes[current]:
            if key not in keys and key < len(boxes):
                keys.add(key)
    
    return (len(opened) == len(boxes))
