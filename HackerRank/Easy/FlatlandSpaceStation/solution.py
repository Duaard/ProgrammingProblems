#!/bin/python3

import math
import os
import random
import re
import sys


def flatlandSpaceStations(n, c):
    # There is only 1 space station
    if len(c) == 1:
        # Check most left and most right city
        return max(c[0], (n - 1) - c[0])

    # There is a space station for each city
    # if len(c) == n:
    #     return 0

    # The max distance
    max_distance = 0
    c.sort()
    # Loop through all space station to check
    # max distance in between it's neigbor station
    # Assuming c[i - i] < c[i] < c[i + 1]
    # 0 1 2 3 4 5
    for i in range(len(c)):
        if i == 0:
            # This is the left most space station
            distance1 = abs(c[i] - ((c[i] + c[i + 1]) // 2))
            distance2 = c[i]
            distance = max(distance1, distance2)
        elif i == len(c) - 1:
            # This is the right most space station
            distance1 = abs(c[i] - math.ceil((c[i] + c[i - 1]) / 2))
            distance2 = (n-1) - c[i]
            distance = max(distance1, distance2)
        else:
            # This space station is in between space stations
            distance1 = abs(c[i] - ((c[i] + c[i + 1]) // 2))
            distance2 = abs(c[i] - math.ceil((c[i] + c[i - 1]) / 2))
            distance = max(distance1, distance2)

        if distance > max_distance:
            max_distance = distance

    return max_distance


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
