#!/bin/python3

import os


def closestNumbers(arr):
    # Sort the array
    arr.sort()
    # Create a map for each absolute difference
    diff = {}
    m = abs(arr[0] - arr[1])
    diff[m] = []

    # Find the min difference by subtracting adjacent pairs
    for i in range(len(arr)):
        if i != len(arr)-1:
            d = abs(arr[i] - arr[i + 1])
            # Check for minimum
            if d < m:
                m = d
                diff[d] = [arr[i], arr[i + 1]]
            elif d == m:
                diff[d].extend([arr[i], arr[i + 1]])

    return diff[m]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
