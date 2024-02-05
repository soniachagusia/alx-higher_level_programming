#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
