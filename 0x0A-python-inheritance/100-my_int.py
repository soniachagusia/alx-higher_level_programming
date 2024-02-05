#!/usr/bin/python3

"""
Contains the class MyInt
"""


class MyInt(int):
    """
    A class representing a rebel integer with inverted equality operators.
    """

    def __init__(self, value):
        """
        Initializes a MyInt instance with the given value.

        Args:
            value: The integer value for MyInt.
        """
        self.value = value
        super().__init__()

    def __eq__(self, other):
        """
        Override the equality operator '==' to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return self.value != other

    def __ne__(self, other):
        """
        Override the inequality operator '!=' to invert its behavior.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return self.value == other
