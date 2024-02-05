#!/usr/bin/python3

"""dds a new attribute to an object
if it’s possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute needs to be added.
        attribute (str): The name of the attribute.
        value: The value of the attribute to be added.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
