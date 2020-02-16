#!/bin/python3

import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    beatiful_counter = 0
    # Loop through all possible i
    for i in arr:
        # Check if i + d exists
        if i + d in arr:
            j = i + d
            # Check if j + d exists
            if j + d in arr:
                # A beatiful triplet for this i exists
                beatiful_counter += 1

    return beatiful_counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
