#!/usr/bin/python3
"""
A module for working with Lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if it's possible to open all the boxes using the provided keys.

    Args:
        boxes (list of lists): sublist represents the keys found in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    opened_boxes = [False] * len(boxes)
    openBox(0, boxes, opened_boxes)
    return all(opened_boxes)


def openBox(box_number, boxes, opened_boxes):
    """
    checks if a box can be opened and unlocks any reachable boxes.

    Args:
        box_number (int): The index of the box to be checked.
        boxes (list of lists): each sublist represents the keys found in a box.
        opened_boxes (list of bool): tracks opened boxes.
    """
    if box_number >= len(boxes) or opened_boxes[box_number]:
        return

    opened_boxes[box_number] = True
    for key in boxes[box_number]:
        openBox(key, boxes, opened_boxes)
