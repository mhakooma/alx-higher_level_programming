#!/usr/bin/python3

"""Looks up the list of available attributes
and methods
"""


def lookup(obj):
    """Returns the list of available attributes
        and methods
        Args:
            obj (object): The object to look up
        Returns:
            A list object
    """
    return (dir(obj))
