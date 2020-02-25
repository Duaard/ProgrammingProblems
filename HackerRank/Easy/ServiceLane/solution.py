#!/bin/python3

import math
import os
import random
import re
import sys


def serviceLane(width, cases):
    # Store all width limits in an array
    width_limit = []
    # Loop through each cases
    for i in cases:
        # Loop through each range to find min width
        min_width = None
        for j in range(i[0], i[1] + 1):
            if min_width is None:
                min_width = width[j]
            if width[j] < min_width:
                min_width = width[j]

        # Append width limit per each case
        width_limit.append(min_width)
    return width_limit


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
