#!/bin/python3

import math
import os
import random
import re
import sys


def superReducedString(s):
    adjacent = True
    # Copy the value of s
    reduced = s
    # While there are still adjacent letters loop
    while adjacent:
        # Set default value to false, only set to true if we find an adjacent pair
        adjacent = False

        # List of index needed to be removed per loop
        remove_index = set([])

        # Loop through each adjacent char
        for i in range(1, len(reduced)):
            # If it has it's left value is the same value
            # and left value doesn't still have a pair
            if reduced[i] == reduced[i - 1] and i-1 not in remove_index:
                # Add this index to indeces to be removed
                remove_index.add(i)
                remove_index.add(i-1)

                # We found an adjacent char
                adjacent = True

        tmp_word = ''
        # Remove each entry in remove index
        for i in range(len(reduced)):
            if i not in remove_index:
                tmp_word += reduced[i]
        reduced = tmp_word

        print(reduced)

    if len(reduced) == 0:
        reduced = 'Empty String'

    return reduced


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
