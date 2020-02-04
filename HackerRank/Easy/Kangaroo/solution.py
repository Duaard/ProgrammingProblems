#!/bin/python3

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    # First case, if k1 starts farther and jumps farther than k2
    # k2 can never catch up, return false
    if v2 >= v1:
        return 'NO'
    d = x2 - x1
    s = v1 - v2
    if d % s != 0:
        return 'NO'
    t = d / s
    if (v1 * t) + x1 == (v2 * t) + x2:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
