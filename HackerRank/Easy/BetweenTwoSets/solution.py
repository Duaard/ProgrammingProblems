#!/bin/python3

import math
import os
import random
import re
import sys


def findLCM(num1, num2):
    if num1 > num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = num1 * num2 / gcd
    print("aa: {}".format(lcm))
    return lcm


def getTotalX(a, b):
    if len(a) == 2:
        lcm = findLCM(a[0], a[1])
    elif len(a) >= 3:
        lcm = findLCM(a[0], a[1])
        for i in range(2, len(arr)):
            lcm = findLCM(lcm, i)
    else:
        lcm = a[0]
    m = min(b)
    mul = lcm
    counter = 0
    while lcm <= m:
        checker = True
        for i in b:
            if i % lcm != 0:
                checker = False
        if checker:
            print(lcm)
            counter += 1
        lcm += mul
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
