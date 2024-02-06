#!/usr/bin/python3


"""defines the write function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the
    number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text content to be written to the file.

    Raises:
        Exception: If the file cannot be opened.

    Returns:
        int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(text)
    except Exception as e:
        raise e
