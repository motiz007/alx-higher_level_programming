#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
    else:
        for row in matrix:
            for item in row:
                print("{:d}".format(item), end="")
            print()
