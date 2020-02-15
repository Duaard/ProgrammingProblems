#!/bin/python3

import math
import os
import random
import re
import sys


def taumBday(b, w, bc, wc, z):
    # If the prices aren't equal
    if bc != wc:
        lesser, greater = ([wc, w], [bc, b]) if wc < bc else ([bc, b], [wc, w])
        # Check if converting is cheaper
        if lesser[0] + z < greater[0]:
            return (lesser[0] + z) * greater[1] + lesser[0] * lesser[1]

    return b * bc + w * wc


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
