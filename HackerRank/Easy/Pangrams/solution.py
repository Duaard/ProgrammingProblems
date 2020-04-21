#!/bin/python3

import os


def pangrams(s):
    # Check if the given string is a pangram

    # Loop through each char in s
    l = []
    for c in "".join(s.split()):
        # Add c to l if it doesn't exist
        if c.lower() not in l:
            l.append(c.lower())

    if len(l) == 26:
        return 'pangram'

    return 'not pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
