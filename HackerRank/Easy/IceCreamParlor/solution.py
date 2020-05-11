#!/bin/python3

import os


def icecreamParlor(m, arr):
    # Loop through each n in arr
    for i, n in enumerate(arr):
        d = m - n
        for j in range(i + 1, len(arr)):
            if d == arr[j]:
                return sorted([i + 1, j + 1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
