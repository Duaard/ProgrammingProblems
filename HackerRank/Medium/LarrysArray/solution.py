#!/bin/python3

import os


def larrysArray(A):
    # Get the number of inversions
    inv = 0
    # Create an array for preceding numbers
    preceding = []
    for num in A:
        # Check all higher preceding numbers
        for p in preceding:
            if p > num:
                # There's an inversion
                inv += 1
        # Add this num to preceding
        preceding.append(num)

    # Check if inversion is even or odd
    if inv % 2 == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
