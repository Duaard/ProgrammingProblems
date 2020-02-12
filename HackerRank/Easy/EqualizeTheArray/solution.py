#!/bin/python3
import os


def equalizeArray(arr):
    # Loop through the array to get the element
    # with most number of occurence
    occurence = {"max": 0}
    for i in range(len(arr)):
        if occurence.get(arr[i]) is None:
            occurence[arr[i]] = 1
        else:
            occurence[arr[i]] += 1
        # Replace max if greater
        if occurence[arr[i]] > occurence["max"]:
            occurence["max"] = occurence[arr[i]]
    # Return the length of array minus the max occurence
    return len(arr) - occurence["max"]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
