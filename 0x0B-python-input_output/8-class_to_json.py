#!/usr/bin/python3

""" Module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing the serializable attributes of the object.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        return {slot: getattr(obj, slot) for slot in obj.__slots__}
    else:
        return obj.__dict__
