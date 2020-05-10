#!/bin/python3

import os


def gameOfThrones(s):
    # Create a dict to track frequency of characters
    f = {}
    # Loop through the populate dict
    for l in s:
        f[l] = f.get(l, 0)
        f[l] += 1

    # Count the number of odd letters
    odd = 0
    # Loop through dict to remove pairs
    for key, val in f.items():
        if val % 2 != 0:
            odd += 1

    if odd > 1:
        return 'NO'
    elif odd == 1 and len(s) % 2 == 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
