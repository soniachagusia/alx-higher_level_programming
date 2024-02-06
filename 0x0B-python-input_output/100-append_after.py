#!/usr/bin/python3

"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search in each line.
        new_string (str): The string to insert after each line
        containing the search string.

    Returns:
        None

    Inserts new_string after each line in the file that
    contains the search_string
    """

    with open(filename, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
