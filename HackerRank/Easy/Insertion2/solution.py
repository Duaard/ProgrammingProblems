#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    # Loop through each element in arr starting from arr[1]
    for elem in range(1, n):
        # Perform insertionSort1
        # Save the last current indexed val
        val = arr[elem]
        # Loop through the array starting from i index to 0
        for i in range(elem, -1, -1):
            # val is greater than the next val
            if arr[i-1] < val or i == 0:
                arr[i] = val
            # else val is still lower, copy the next val to current index
            else:
                arr[i] = arr[i-1]

            # If the current index is the place of val
            if (arr[i] == val):
                # Stop the loop
                break
        # Print the sorted arr
        for num in arr:
            print(num, end=' ')
        print()


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
