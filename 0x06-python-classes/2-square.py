#!/usr/bin/python3

"""
Square Class

This class defines a square and encapsulates its size attribute.
"""


class Square:
    """
    Represents a Square object with a defined size attribute.

    Attributes:
        __size (int): Represents the size of a side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a specified size.

        Args:
            size (int): The size of a side of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
