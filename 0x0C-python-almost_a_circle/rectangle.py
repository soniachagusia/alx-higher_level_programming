#!/usr/bin/python3
"""
Module for Rectangle class.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from Base class.

    Attributes:
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): x coordinate of the rectangle.
        __y (int): y coordinate of the rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x coordinate of the rectangle. Defaults to 0.
            y (int): y coordinate of the rectangle. Defaults to 0.
            id (int): Unique identifier. Defaults to None.

         Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x coordinate."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y coordinate."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """String representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes of the Rectangle."""
        if args:
            attr_list = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __validate_int(self, attr_name, value):
        """Validates if the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")

    def __validate_positive(self, attr_name, value):
        """Validates if the value is a positive integer."""
        if value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def __validate_non_negative(self, attr_name, value):
        """Validates if the value is a non-negative integer."""
        if value < 0:
            raise ValueError(f"{attr_name} must be >= 0")

    def to_dictionary(self):
        """
        Returns a dictionary representation of the rectangle.

        Returns:
            dict: A dictionary containing the rectangle's attributes.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
