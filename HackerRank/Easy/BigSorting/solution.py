#!/bin/python3

import math
import os
import random
import re
import sys


def bigSorting(unsorted):
    # Store the len per each elem
    len_dict = {}

    sorted_list = []

    # Loop through each element to store their len
    for val in unsorted:
        if len(val) not in len_dict:
            # Create a new entry in dict
            len_dict[len(val)] = [val]
        else:
            # Append to existing entry
            len_dict[len(val)].append(val)

    # Get the different lengths and sort it
    keys = list(len_dict.keys())
    keys.sort()

    # Sort per each len and EXTEND to sorted_list
    for key in keys:
        len_dict[key].sort()
        sorted_list.extend(len_dict[key])

    return sorted_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
