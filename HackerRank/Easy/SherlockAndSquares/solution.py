#!/bin/python3

import math
import os
import random
import re
import sys


def squares(a, b):
    # First look at the lowest possible square integer
    lo = math.ceil(math.sqrt(a))
    # Look for the highest possible square integer
    hi = math.floor(math.sqrt(b))
    # Return the length of range of the lo and hi
    return len(range(lo, hi + 1))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
