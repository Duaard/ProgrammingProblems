#!/bin/python3

import math
import os
import random
import re
import sys


def alternate(s):
    if len(s) < 2:
        return 0

    # Get all characters present in s
    char_list = []
    for c in s:
        if c not in char_list:
            char_list.append(c)

    # Check if there's only one type of letter
    if len(char_list) < 2:
        return 0

    # Keep track of all possible combination in char_list
    combi = {}

    for i in range(len(char_list) - 1):
        for j in range(i + 1, len(char_list)):
            # Convert index to letter
            c1 = char_list[i]
            c2 = char_list[j]

            # Create entry for c1
            combi[c1] = {} if c1 not in combi else combi[c1]
            # Create entry for c2
            combi[c2] = {} if c2 not in combi else combi[c2]
            # Create c entry for j to know where it's attached
            combi[c2]['under'] = [
                c1] if 'under' not in combi[c2] else combi[c2]['under'] + [c1]
            # Initalize empty array per each combination
            combi[c1][c2] = []

    # Pairs that contain repeating char
    remove = []

    # Loop through each char in s updating every combination it's part of
    for c in s:
        # Update every combination under this c
        for pair in combi[c]:
            if pair != 'under':
                # Check if this pair repeated
                if len(combi[c][pair]) > 0 and c == combi[c][pair][-1]:
                    # Remove this pair
                    remove.append([c, pair])
                else:
                    # Add entry to this pair
                    combi[c][pair].append(c)

            else:
                remove_under = []
                # Go through each pair this c is under
                for u in combi[c]['under']:
                    # Check if this pair is repeated
                    if len(combi[u][c]) > 0 and c == combi[u][c][-1]:
                        # Remove this pair
                        remove.append([u, c])
                    else:
                        # Add entry to this pair
                        combi[u][c].append(c)

    for rem in remove:
        if rem[0] in combi:
            if rem[1] in combi[rem[0]]:
                del(combi[rem[0]][rem[1]])

    # Get the longest possible string
    longest = 0

    for key in combi:
        for pair in combi[key]:
            if pair != 'under':
                if len(combi[key][pair]) > longest:
                    longest = len(combi[key][pair])

    return longest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
