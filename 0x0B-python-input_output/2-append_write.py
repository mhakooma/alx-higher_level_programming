#!/usr/bin/python3

"""Appends text to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file
    Args:
        filename (str): The filename to append to
        text (str): The text to append
    Returns:
        The number of characters added
    """
    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)
