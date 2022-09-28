#!/usr/bin/python3

"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): class to match
    Returns:
        True if obj is an instance or inherited of a_class
        False if otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
