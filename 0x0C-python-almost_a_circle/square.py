#!/usr/bin/python3

"""Module Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Updates attributes"""
        attrs = ["id", "size", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def to_dictionary(self):
        """Returns dictionary representation of Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
