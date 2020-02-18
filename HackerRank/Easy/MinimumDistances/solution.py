#!/bin/python3

import math
import os
import random
import re
import sys


def minimumDistances(a):
    # Map used to store values from a
    distanceMap = {}
    minDistance = None
    # Loop through the entire array
    # O(n) complexity
    for i in range(len(a)):
        # Check if value does not exists in map
        if a[i] not in distanceMap:
            # Register current index
            distanceMap[a[i]] = i
        else:
            # Calculate distance from previous index
            dist = i - distanceMap[a[i]]
            # Check if lower than existing min val
            if minDistance is None or dist < minDistance:
                minDistance = dist
            # Check if min is already at least value
            if minDistance == 1:
                break
            # Register latest index
            distanceMap[a[i]] = i
    # Check if minDistance exists
    if minDistance:
        return minDistance
    else:
        return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
