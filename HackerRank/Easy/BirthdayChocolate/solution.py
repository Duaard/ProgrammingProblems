#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):
    # Loop the range minus the last bits
    # since we need a continuous segment
    counter = 0
    for i in range(len(s) - m + 1):
        sum = 0
        for j in range(m):
            sum += s[i + j]
        if d == sum:
            counter += 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
