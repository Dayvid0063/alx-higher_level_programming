#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    num = matrix.copy()
    for u in range(len(matrix)):
        num[u] = list(map(lamda x: x**2, matrix[u]))
        return num
