#!/usr/bin/python3
"""module containing a function that returns the JSON
representation of an object
"""

import json


def to_json_string(my_obj):
    """
    Converts the given object to its JSON string representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        A JSON string representing the object.

    """
    return json.dumps(my_obj)
