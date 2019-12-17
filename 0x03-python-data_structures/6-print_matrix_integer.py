#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for idx, row in enumerate(matrix, 1):
            for idx, i in enumerate(row, 1):
                if idx < len(row):
                    print("{:d} ".format(i), end="")
                else:
                    print("{:d}".format(i))
