#!/usr/bin/python3

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle with n rows.

    Args:
        n (int): Number of rows in the Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.

    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
