#!/usr/bin/python3

"""Converts objects to JSON"""

import json


def to_json_string(my_obj):
    """Converts an object  to JSON

    Args:
        my_obj: The object to convert
    Returns:
        string representation of the object
    """
    return json.dumps(my_obj)
