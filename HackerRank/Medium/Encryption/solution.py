#!/bin/python3

import math
import os


def encryption(s):
    # Remove white space
    l = ''.join(s.split())

    # Get number of row and col
    r = math.floor(math.sqrt(len(l)))
    c = math.ceil(math.sqrt(len(l)))
    if r * c < len(l):
        r += 1

    # Encrypted string
    enc = ''

    # Loop through all the cols
    for col in range(c):
        word = ''
        # Loop through all the rows
        for row in range(r):
            index = col + (row * c)
            if index < len(l):
                word += l[index]

        enc += word + ' '

    return enc.rstrip()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
