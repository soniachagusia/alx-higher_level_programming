#!/usr/bin/python3

""" Module that contains a function that returns an object by
a JSON representation
"""

import json


def from_json_string(my_str):
    """
    Converts the given JSON string to a Python object (data structure).

    Args:
        my_str: The JSON string to be converted.

    Returns:
        A Python object representing the JSON data.

    """
    return json.loads(my_str)
