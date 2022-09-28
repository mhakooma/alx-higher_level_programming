#!/usr/bin/python3

"""
Reads a text file
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints to stdout
    Args:
        filename (str): path to the file to read
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
