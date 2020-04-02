#!/bin/python3

import os


def camelcase(s):
    # Loop through each character and count all uppercase leeetters
    counter = 0
    for c in s:
        if c.isupper():
            counter += 1
    # Return the counter + 1
    return counter + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
