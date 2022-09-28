#!/usr/bin/python3

"""Defines a save-to-JSON function"""

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation

    Args:
        my_obj (object): The object to write to file
        filename (str): The name of the file to write to
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
