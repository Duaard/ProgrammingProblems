#!/bin/python3

import math
import os
import random
import re
import sys


def chocolateFeast(n, c, m):
    # Get the total chocolates Bobby can buy with the initial money
    chocolates = n // c
    wrappers = chocolates

    # While you can still convert your wrappers to chocolates
    while wrappers >= m:
        # Convert wrappers into chocolates
        new_chocolates = wrappers // m
        # Set the remaining wrappers
        wrappers = wrappers % m + new_chocolates
        # Add new chocolates to total chocolates
        chocolates += new_chocolates

    return chocolates


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
