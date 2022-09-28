#!/usr/bin/python3

"""Checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if an object is exact match of a class
    Args:
        obj (any): object to check
        a_class (type): class to match
    Returns:
        True if obj is an instance of a_class
        False if otherwise
    """
    if type(obj) == a_class:
        return True
    return False
