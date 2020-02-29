#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    # If k is 1, arr[0] is the special number
    # as the first chapter will be the only one to
    # start with same inital value sa page
    if k == 1:
        return arr[0]
    special_problems = 0
    # Start the page on 1
    page = 1
    for problems in arr:
        # Get how many pages these problem will take up
        end_page = page + math.ceil(problems / k) - 1
        # At what page will index catch up to page
        # computed using d / s then adjusted value for t0
        catchup = page + max(math.ceil((page - 1) / (k-1)) - 1, 0)
        print(
            f'page: {page}, end_page: {end_page}, catchup: {catchup}, prob: {problems}')
        # Check if catchup is within the range of pages and within range of problem
        if (catchup <= end_page and catchup <= problems):
            # Special problem will occur
            special_problems += 1
            print('SPECIAL!')
            # Check if the special problem is at the most bottom index
            # And next page still within end page
            if (catchup % k == 0 and catchup + 1 <= end_page and catchup + 1 <= problems):
                print('DOUBLE SPECIAL')
                # Another special problem will occur
                special_problems += 1
        page = end_page + 1
    print(f'special numbers: {special_problems}')
    return special_problems


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
