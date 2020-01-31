#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    size = len(arr[0]) - 1
    diag1 = 0
    diag2 = 0
    ad = 0
    for x in arr:
        for i in range(size+1):
            if i == ad:
                diag1 += x[i]
            if i == size - ad:
                diag2 += x[i]
        ad += 1
    return abs(diag1 - diag2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
