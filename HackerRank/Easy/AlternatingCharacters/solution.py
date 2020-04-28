#!/bin/python3

import os


def alternatingCharacters(s):
    # Count the number of consecutive characters
    prev = ''
    cntr = 0
    for c in s:
        if c == prev:
            cntr += 1

        prev = c
    return cntr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
