#!/bin/python3

import math
import os
import random
import re
import sys


def cutTheSticks(arr):
    # Initial stick size
    ans = [len(arr)]

    while(len(arr) != 0):
        # Make a copy of the arr
        sticks = arr.copy()
        # Get the shortest
        shortest = min(sticks)
        for i in range(len(sticks)):
            value = sticks[i]
            sticks[i] -= shortest
            if (sticks[i] <= 0):
                # Remove this stick from the original arr
                arr.remove(value)
        # Get the remaining sticks
        if (len(arr) != 0):
            ans.append(len(arr))
    return ans

    while(len(arr) != 0):
        # Make a list of sticks to discard per iteration
        discarded_sticks = []
        shortest = min(arr)
        # Loop through all sticks and cut them by shortest
        for i in range(len(arr)):
            arr[i] -= shortest
            if arr[i] <= 0:
                # Remove it from the array
                discarded_sticks
        # Remove sticks
        for i in range(len(discarded_sticks)):
            arr.pop(discarded_sticks[i])
        # Save the number of remaning sticks
        ans.append(len(arr))
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
