#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    # Store the value in an array
    ans = []
    # From 1 to n, get it's p(y) and p(p(y))
    for i in range(1, len(p) + 1):
        # Get p(y), the index of i + 1
        p_of_y = p.index(i) + 1
        # Look for y
        y = p.index(p_of_y)
        # Add 1 to offset
        ans.append(y + 1)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
