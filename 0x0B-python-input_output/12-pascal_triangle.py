#!/usr/bin/python3
"""
returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    function that impliment teh pascla triangle 
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
