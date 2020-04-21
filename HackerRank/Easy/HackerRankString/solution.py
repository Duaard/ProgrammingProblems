#!/bin/python3

import os


def hackerrankInString(s):
    # Checks if a string contains 'hackerrank' in order
    w = 'hackerrank'

    # Loop through each char in the string
    i = 0
    for c in s:
        if c == w[i]:
            # Move too the next index
            i += 1
        if i == len(w):
            # All letters were found
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
