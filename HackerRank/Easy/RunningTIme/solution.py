#!/bin/python3

import math
import os
import random
import re
import sys


def runningTime(arr):
    # Record the number of shifts performed
    shifts = 0
    # Loop through each element in arr starting from arr[1]
    for elem in range(1, len(arr)):
        # Save the current indexed val
        val = arr[elem]
        # Loop through the array starting from elem index to 0
        for i in range(elem, -1, -1):
            # val is greater than equal the next val
            if arr[i-1] <= val or i == 0:
                arr[i] = val
            # else val is still lower, copy the next val to current index
            else:
                arr[i] = arr[i-1]
                # Record shift
                shifts += 1

            # If the current index is the place of val
            if (arr[i] == val):
                # Stop the loop
                break

    # Return the number of shifts
    return shifts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
