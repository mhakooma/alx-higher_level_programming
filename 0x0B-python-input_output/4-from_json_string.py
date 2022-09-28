#!/usr/bin/python3

"""Defines a JSON-to-objects function"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string

    Args:
        my_str: The JSON string
    Returns:
        object representation of the JSON string
    """
    return json.loads(my_str)
