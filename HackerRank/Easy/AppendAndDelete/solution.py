#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    equal_substring = 0
    # Set the length to the shorter string
    length = len(s) if len(s) < len(t) else len(t)
    # Find how many first equal char s and t have
    for i in range(length):
        if s[i] == t[i]:
            equal_substring += 1
        else:
            break
    # Disregard unequal characters
    k -= len(s) - equal_substring

    # Remove unneeded k moves
    unneeded = k - (len(t) - equal_substring)
    while (unneeded > 0):
        # Disregard until k is no longer > 0
        k -= 1
        # Clamp value to 0, you can't have negative equal_substring
        equal_substring = max(0, equal_substring - 1)
        unneeded = k - (len(t) - equal_substring)

    # Append needed characters
    k -= len(t) - equal_substring

    # Check if possible with k moves
    if k >= 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
