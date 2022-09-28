#!/usr/bin/python3

"""Writes a string to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns
        the number of characters written
    Args:
        filename (str): The filename to write to
        text (str): The string to write
    Returns:
        number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
