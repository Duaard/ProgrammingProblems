#!/bin/python3

import math
import os
import random
import re
import sys


def happyLadybugs(b):
    occurence = {}
    # Used to check if lady bugs are happy as is
    happy = True
    last_char = ''
    threshold = 0

    # Loop through each char in the board to populate dict
    for i in range(len(b)):
        if b[i] in occurence:
            occurence[b[i]] += 1
        else:
            occurence[b[i]] = 1
        if last_char != b[i] and b[i] != '_':
            threshold += 1
        else:
            threshold = 0
        if threshold >= 2:
            happy = False
        last_char = b[i]
    print(occurence)
    # Check if there's one lady bug
    for key, val in occurence.items():
        if val == 1 and key != '_':
            print('first check!')
            return 'NO'

    # No empty cell and not all are happy
    if '_' not in occurence and not happy:
        print('second check!')
        return 'NO'

    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
