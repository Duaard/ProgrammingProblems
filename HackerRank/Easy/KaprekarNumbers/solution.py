#!/bin/python3

import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    valid_range = False
    # Loop through the range, O(n)
    for i in range(p, q + 1):
        sqr = i * i
        d = len(str(i))
        # Get the last d numbers of sqr
        r = int(str(sqr)[d * -1:])
        l = 0
        # Get the rest of the numbers
        if len(str(r)) != len(str(sqr)):
            l = int(str(sqr)[0:len(str(sqr)) - d])
        # Check if i is a kaprekarNum
        if r + l == i:
            print(i, end=' ')
            if not valid_range:
                valid_range = True
    if not valid_range:
        print('INVALID RANGE')


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
