#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # Initial jump
    start = True
    i = 0
    e = 100
    while(start or i != 0):
        # Turn off start
        start = False
        # Make a jump
        i = (i + k) % len(c)
        # Deduct the jump to your energy
        if(c[i] == 0):
            # This is a cumulus
            e -= 1
        else:
            # This is a thunderhead
            e -= 3
    # Return energy left
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
