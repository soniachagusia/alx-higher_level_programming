#!/usr/bin/python3

""" Module that creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, 'r') as file:
        data = json.load(file)

    return data
