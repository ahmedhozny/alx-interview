# Lockboxes

This Python code tackles the problem of determining if all lockboxes can be opened using the provided keys. Here's how it works:

    canUnlockAll(boxes) function:
        It initializes a list opened_boxes to track the open/closed state of each box (True for open, False for closed).
        It calls the helper function openBox recursively, starting from the first box (index 0).
        After all boxes are checked, it returns True if all boxes in opened_boxes are marked True (opened), signifying all boxes were unlocked. Otherwise, it returns False.

    openBox(box_number, boxes, opened_boxes) function (recursive):
        It checks if the current box (box_number) is already marked opened in opened_boxes. If so, it avoids revisiting to prevent infinite recursion.
        If the box is unopened, it marks it as opened in opened_boxes.
        It iterates through the list of keys found in the current box (boxes[box_number]).
        For each key, it recursively calls itself (openBox) to check if the corresponding box (identified by the key) can be opened using its own keys. This creates a chain reaction, exploring all reachable boxes.

By recursively following the trails of keys, this function simulates unlocking boxes. If it encounters a locked box with no accessible key, the recursion terminates, and canUnlockAll returns False. If all boxes are eventually opened, canUnlockAll returns True.