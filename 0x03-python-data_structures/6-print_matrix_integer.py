#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for u in range(len(matrix)):
            for v in range(len(matrix[u])):
                if v != len(matrix[u]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                    print("{:d}".format(matrix[u][v]), end=endspace)
                    print()
