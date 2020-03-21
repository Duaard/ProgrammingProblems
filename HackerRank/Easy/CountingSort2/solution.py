#!/bin/python3
import os


def countingSort(arr):
    # Sort an array without comparison

    # Get the highest value possible in array
    # 100 in the input constraints
    hi = 100

    # Create a 0 array spanning the range of arr values
    counter = [0] * hi

    # Loop through the array and record each count
    for i in range(len(arr)):
        counter[arr[i]] += 1

    sorted_arr = []
    # Loop through each value in counter and add to approp sorted_arr
    for i in range(hi):
        sorted_arr.extend([i] * counter[i])

    return sorted_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
