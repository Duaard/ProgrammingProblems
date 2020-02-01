#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n, p, z = 0, 0, 0
    s = len(arr)
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    print("{0:.6f}".format(p/s))
    print("{0:.6f}".format(n/s))
    print("{0:.6f}".format(z/s))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)