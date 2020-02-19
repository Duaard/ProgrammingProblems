#!/bin/python3

import math
import os
import random
import re
import sys


def getDiff3x3(matrix1, matrix2):
    # Gets the total difference between two 3 x 3 matrices
    total = 0
    for i in range(3):
        for j in range(3):
            diff = abs(matrix1[i][j] - matrix2[i][j])
            total += diff
    return total


def formingMagicSquare(s):
    # List of all possible magic squares
    magic_square_str = ['816357492',
                        '618753294', '492357816', '294753618', '834159672',
                        '438951276', '672159834', '276951438']
    magic_square = []
    for i in magic_square_str:
        # Parse the str and add to magic_square
        matrix = []
        for k in range(3):
            row = []
            for l in range(3):
                row.append(int((i[(k * 3) + l])))
            matrix.append(row)
        magic_square.append(matrix)

    least_dif = None
    # Find the least difference
    for i in magic_square:
        dif = getDiff3x3(i, s)
        if least_dif is None or dif < least_dif:
            least_dif = dif
    return least_dif


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
