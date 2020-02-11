#!/bin/python3

import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    jumps = 0
    i = 0
    # Loop through the clouds
    while i < len(c)-1:
        # Check if the next next cloud is 0 and within range
        if (i+2 <= len(c) - 1 and c[i+2] == 0):
            # Move twice
            jumps += 1
            i += 2
        else:
            # Move once
            jumps += 1
            i += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
