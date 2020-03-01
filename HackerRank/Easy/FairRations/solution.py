#!/bin/python3

import math
import os
import random
import re
import sys


def fairRations(B):
    odd_bread = []
    # Check the number of odd loaves
    # and add their index to index liste
    for i in range(len(B)):
        if B[i] % 2 != 0:
            odd_bread.append(i)

    # If the number of odd is odd return NO
    if len(odd_bread) % 2 != 0:
        return 'NO'
    else:
        loaves = 0
        # Find the min number of loaves by finding it's nearest odd pair
        for i in range(0, len(odd_bread), 2):
            # Find the distance between this pair
            dist = abs(odd_bread[i] - odd_bread[i + 1])
            # The number of loaves to make this pair even is the dist * 2
            loaves += dist * 2

    return loaves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
