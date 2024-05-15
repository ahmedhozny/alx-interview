#!/usr/bin/python3
"""
A module for validating UTF-8 encoding.
"""

def validUTF8(data):
    """
    Determines if a given list of integers represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers representing bytes (0 to 255).

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    next_span = 0
    for byte in data:
        if next_span == 0:
            next_span = get_span(byte)
            if next_span == -1:
                return False
        else:
            if not check_continuity(byte):
                return False
            next_span -= 1
    return True


def get_span(byte):
    """
    Determines the number of bytes in a UTF-8 encoded character
    based on the first byte.

    Args:
        byte (int): The first byte of a UTF-8 character.

    Returns:
        int: The number of remaining bytes in the UTF-8 character
        (0, 1, 2, or 3), or -1 if the byte is not a valid starting byte.
    """
    if byte < 128:
        return 0
    if byte < 192:
        return -1
    if byte < 224:
        return 1
    if byte < 240:
        return 2
    if byte < 248:
        return 3
    return -1


def check_continuity(byte):
    """
    Checks if a byte is a valid continuation byte in UTF-8 encoding.

    Args:
        byte (int): The byte to check.

    Returns:
        bool: True if the byte is a valid continuation byte, False otherwise.
    """
    return 128 <= byte <= 192
