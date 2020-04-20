#!/bin/python3


def reverse(arr):
    # Reverses an array
    for i in range(len(arr) // 2):
        tmp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = tmp


def almostSorted(arr):
    # Identify how many numbers are out of order
    d = []
    sorted_arr = arr.copy()
    sorted_arr.sort()

    for i in range(len(arr)):
        # Check if this num is out of place
        if sorted_arr[i] != arr[i]:
            d.append(i)

    if len(d) == 0:
        print('yes')
    elif len(d) == 2:
        print('yes')
        print('swap {} {}'.format(d[0] + 1, d[1] + 1))
    else:
        # Check if the arr can be sorted by reversing
        sl = arr[d[0]:d[len(d)-1] + 1]
        reverse(sl)
        if sl == sorted(sl):
            print('yes')
            print('reverse {} {}'.format(d[0] + 1, d[len(d) - 1] + 1))
        else:
            print('no')


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
