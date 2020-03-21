#!/bin/python3


def countSort(arr):
    # Prints the sorted string of based on it's accompanying int

    # Set the hi, for this case 100
    hi = 100

    # Create the count arr
    count = [[] for i in range(hi)]

    # Get the half of arr for conversion to '-'
    half = len(arr) / 2

    # Loop through the array to perform countsort
    for i, [x, s] in enumerate(arr):
        # Perform conversion
        if i < half:
            s = '-'
        count[int(x)].append(s)

    result = ''
    for i in count:
        # Get each array of char and append to result
        if len(i) > 0:
            result += ' '.join(i) + ' '

    result = result.rstrip()

    print(result)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
