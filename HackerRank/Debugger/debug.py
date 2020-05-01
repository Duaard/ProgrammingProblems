#!/bin/python3

import os


def closestNumbers(arr):
    # Create a map for each absolute difference
    diff = {}
    m = abs(arr[0] - arr[1])
    diff[m] = []

    # Populate the map with every pair and check for min
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            # Create a value for this pair
            d = abs(arr[i] - arr[j])
            print(d)
            # Check for minimum
            # if d < m:
            #     m = d
            #     diff[d] = [arr[i], arr[j]]
            # elif d == m:
            #     diff[d].extend([arr[i], arr[j]])

    return diff[m]


if __name__ == '__main__':
    fptr = open('./out.txt', 'w')
    f = open('./in.txt', 'r')

    n = int(f.readline())

    arr = list(map(int, f.readline().rstrip().split()))

    f.close()

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
