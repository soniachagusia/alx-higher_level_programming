<<<<<<< HEAD
#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): The first number.
    b (int or float): The second number. Defaults to 98.

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
=======
#!/usr/bin/python3
"""My addition module

add_integer: adds two integers together

"""


def add_integer(a, b=98):
    """Returns a + b
    Args: a and b (int): the numbers to add
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
>>>>>>> cca8ce93ee76cfdf7338b7958dbc375e40c013e1
