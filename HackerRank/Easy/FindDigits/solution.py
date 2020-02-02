#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    ans = 0
    # Convert the n to str to get the digits
    for digit in str(n):
        # Convert back the digit to int and perform equation
        if int(digit) != 0 and n % int(digit) == 0:
            ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
