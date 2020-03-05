#!/bin/python3

import math
import os
import random
import re
import sys


def strangeCounter(t):
    # f(t) = log (t+2/3)
    # f(x) = 3 * 2 ^ f(t)

    # Find f(t), needed to find the intial value the cycle this t belongs
    f_of_t = math.log2((t + 2) / 3)
    # Find the inital value using the floor or f_of_t then finding it's f(x)
    x = math.floor(f_of_t)
    # Find f(x)
    i_value = (3 * pow(2, x))
    # Find t of inital by deducting 2
    i_place = i_value - 2

    # Subtract to the initial value the difference in i_place and t
    counter = i_value - (t - i_place)

    # Return the value
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
