#!/usr/bin/python3


"""defines the function that appends to line"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to append to or create.
        text (str): The text content to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
