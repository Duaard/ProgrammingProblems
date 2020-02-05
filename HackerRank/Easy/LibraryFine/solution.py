#!/bin/python3

import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    # First case: returned on or before
    # fine = 0
    if (y1 < y2 or (y1 == y2 and m1 < m2) or (y1 == y2 and m1 == m2 and d1 <= d2)):
        return 0
    # Second case: returned within same month
    # fine = 15 x n_days_late
    elif (y1 == y2 and m1 == m2):
        return 15 * (d1 - d2)
    # Third case: returned within same year
    # fine = 500 x n_months_late
    elif (y1 == y2):
        return 500 * (m1 - m2)
    # Fourth case: returned with different year
    # fine = 10000
    else:
        return 10000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
