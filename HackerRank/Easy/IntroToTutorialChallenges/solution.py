#!/bin/python3

import math
import os
import random
import re
import sys


def binarySearch(V, arr):
    # Recursive function to search for index of V in arr
    # Look for the middle index
    mid = len(arr) // 2
    # V is in the left side of the arr
    if V < arr[mid]:
        # Perform binary search on the left side of arr
        return binarySearch(V, arr[:mid])
    # V is in the right side of the arr
    elif V > arr[mid]:
        # Perform binary search on the right side of arr
        return mid + 1 + binarySearch(V, arr[mid+1:])
    # V is in the middle
    else:
        return mid


def introTutorial(V, arr):
    # Look for index of v in arr
    # Since arr is sorted we can perform a binary search
    return binarySearch(V, arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
