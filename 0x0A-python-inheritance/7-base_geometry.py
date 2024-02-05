#!/usr/bin/python3

"""
Module: 7-base_geometry

Contains the BaseGeometry class with area() and integer_validator() methods.
"""


class BaseGeometry:
    """
    A class representing basic geometry.
    """

    def area(self):
        """
        Raises an exception with the message 'area() is not implemented'.

        Raises:
            Exception: Always raises an exception.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the given value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
