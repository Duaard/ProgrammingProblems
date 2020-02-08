#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    birds = {}
    for i in arr:
        if i not in birds:
            birds[i] = 1
        else:
            birds[i] += 1

    h_id = 6
    h = 0
    print(birds)
    for key in birds:
        if birds[key] > h:
            h = birds[key]
            h_id = key
        elif birds[key] == h and key < h_id:
            h = birds[key]
            h_id = key
    return h_id


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
