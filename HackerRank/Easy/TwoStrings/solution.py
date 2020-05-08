#!/bin/python3

import os


def twoStrings(s1, s2):
    # Return results based on wether s1 and s2 has common elements
    i = set(s1).intersection(set(s2))
    if len(i) > 0:
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
