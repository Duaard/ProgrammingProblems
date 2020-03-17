#!/bin/python3

import math
import os
import random
import re
import sys


def quickSort(arr):
    # Get the pivot number
    pivot = arr[0]

    # Save all the subsets for each array
    left, equal, right = [], [], []

    # Loop through the array to get each subset
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)
    # Combine all 3 subsets
    sorted_arr = left + equal + right

    return sorted_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
