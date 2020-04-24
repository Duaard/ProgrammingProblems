#!/bin/python3

import os


def reverse(s):
    # Reverses a list
    return [r for r in reversed(s)]


def funnyString(s):
    # Get the reverse of s
    r = reverse(s)

    # Loop through to find the abs diff
    for i in range(len(s)):
        if i != 0:
            diff1 = abs(ord(s[i]) - ord(s[i-1]))
            diff2 = abs(ord(r[i]) - ord(r[i-1]))
            if diff1 != diff2:
                return 'Not Funny'
    return 'Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
