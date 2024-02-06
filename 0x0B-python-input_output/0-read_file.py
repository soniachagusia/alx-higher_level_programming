#!/usr/bin/python3

""" Defines the function read"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.

    Note:
        You must use the 'with' statement.
        You don’t need to manage file permission or file doesn'texist exception
        You are not allowed to import any module.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
