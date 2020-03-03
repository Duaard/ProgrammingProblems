#!/bin/python3

import math
import os
import random
import re
import sys


def stones(n, a, b):
    # Find all the possible last values
    last_values = []

    # The number of non_zero stones
    nonzero = n - 1

    # If the difference are equal there's only one last value
    if a == b:
        return [a * nonzero]

    # Combination with repetition using n and 2 (a,b)
    # (n+r-1)!/r!(n-1)!
    # in this case upper permutation will just cancel lower permutation as
    # (n + 1)! / n! so c = n + 1
    c = nonzero + 1
    # Loop through each possible combination adjusting number of a and b
    for i in range(c):
        last_val = (a * (nonzero - i)) + (b * i)
        last_values.append(last_val)
    last_values.sort()
    return last_values


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
