#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, arr):
    counter = 0
    for i in range(n):
        for j in range(n):
            if i < j and (arr[i] + arr[j]) % k == 0:
                counter += 1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
