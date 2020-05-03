#!/bin/python3

import os
import math


def theLoveLetterMystery(s):
    # Check if the string is already palindrome
    h = math.ceil(len(s)/2)
    l = len(s) // 2
    if s[:l] == s[h:][::-1]:
        return 0

    # Check what letters doesn't make it one
    operations = 0
    for i in range(l):
        # Compare i to its corresponding inverse
        inv = len(s)-1-i
        if s[i] != s[inv]:
            # Calculate the number of operations needed
            operations += abs(ord(s[i]) - ord(s[inv]))
    return operations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
