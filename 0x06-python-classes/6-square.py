#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square.

    Attributes:
        __size (int): Size of a side of the square.
        __position (tuple): Position of the square in 2D space.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square.

        Args:
            size (int): Size of a side of the square.
            position (tuple): Position of the square in 2D space.

        Raises:
            TypeError: If size is not an integer or position is not a tuple
            ValueError: If size is less than 0 or position contains value

        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the square's area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter for __size.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size.

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

    def my_print(self):
        """Prints the square.

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Getter for __position.

        Returns:
            The position of the square in 2D space.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for __position.

        Args:
            value (tuple): Position of the square in 2D space.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If value contains values less than 0.

        Returns:
            None
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
