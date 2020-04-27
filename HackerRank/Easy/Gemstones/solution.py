#!/bin/python3

import os


def gemstones(arr):
    # Create the set that will hold all intersection
    gemStones = None
    for a in arr:
        if gemStones == None:
            gemStones = set(a)
        else:
            gemStones = gemStones & set(a)
    return len(gemStones)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
