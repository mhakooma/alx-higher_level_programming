#!/usr/bin/python3

"""Defines a load-from-JSON function"""

import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”
    Args:
        filename (str): The JSON file to load
    """
    with open(filename) as f:
        return json.load(f)
