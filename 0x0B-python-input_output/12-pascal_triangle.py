#!/usr/bin/python3
"""func returns lists of integers representing the Pascal triangle"""


def pascal_triangle(n):
    """Pascal Triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        v = triangles[-1]
        elem = [1]
        for u in range(len(v) - 1):
            elem.append(v[u] + v[u + 1])
        elem.append(1)
        triangles.append(elem)
    return triangles
