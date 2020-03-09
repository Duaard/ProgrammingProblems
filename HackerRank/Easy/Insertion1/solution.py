#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    sorted_arr = arr.copy()
    # Save the last indexed val
    val = arr[n-1]

    # Loop through the array starting from the greatest val index to 0
    for i in range(n - 1, -1, -1):
        # val is greater than the next val
        if arr[i-1] < val or i == 0:
            sorted_arr[i] = val
        # else val is still lower, copy the next val to current index
        else:
            sorted_arr[i] = sorted_arr[i-1]
        # Print the current state of sort
        for num in sorted_arr:
            print(num, end=' ')
        print()

        if (sorted_arr[i] == val):
            # Stop the loop
            break


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
