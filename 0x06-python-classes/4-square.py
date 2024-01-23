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
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): Size of a side of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
