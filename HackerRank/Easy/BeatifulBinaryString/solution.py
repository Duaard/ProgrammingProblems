#!/bin/python3

import os


def beautifulBinaryString(b):
    # Count how many times the substring 010 occurs in b
    return b.count('010')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
