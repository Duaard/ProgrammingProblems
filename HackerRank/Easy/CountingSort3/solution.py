#!/bin/python3
import os


def countList(arr, hi):
    # Returns a list containing frequency of each num starting from hi

    # Create a 0 array spanning the range of arr values
    counter = [0] * hi

    # Loop through the array and record each count
    for i in range(len(arr)):
        counter[int(arr[i][0])] += 1

    return counter


def getOccurenceCombined(arr):
    # Return a list of L's from 0-99
    hi = 100
    L = [0] * hi
    counter = countList(arr, hi)

    for i in range(hi):
        if i != 0:
            # Combine the count plus previous count
            L[i] = L[i - 1] + counter[i]
        else:
            L[i] = counter[i]

    return L


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = [input().rstrip().split() for i in range(n)]
    result = getOccurenceCombined(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
