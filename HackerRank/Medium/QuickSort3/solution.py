#!/bin/python3


def quick_sort(ar, lo, hi):
    if lo < hi:
        [ar, i] = partition(ar, lo, hi)
        # Sort the left sub array
        ar = quick_sort(ar, lo, i - 1)
        # Sort the right sub array
        ar = quick_sort(ar, i + 1, hi)
    return ar


def partition(ar, lo, hi):
    # Partitions an ar using the last element as pivot and
    # in place method through keeping track of lesser values through i

    # Get the pivot
    pivot = ar[hi]

    # Set the default value for i
    # indicating the pos of pivot
    i = lo
    # Loop through the array to partition
    for j in range(lo, hi + 1):
        if ar[j] < pivot:
            # Swap ar[i] and ar[j]
            tmp = ar[i]
            ar[i] = ar[j]
            ar[j] = tmp
            # Increment pos of i
            i += 1
    # Put the pivot in the right place by swapping
    # it's pos and the current i
    tmp = ar[i]
    ar[i] = pivot
    ar[hi] = tmp

    if lo < hi:
        [print(x, end=' ') for x in ar]
        print()

    # The ar is now partitioned
    # Return the partitioned arr and pos of i
    return [ar, i]


# Get the size of array
n = int(input())
# Get the array
ar = list(map(int, input().split()))

quick_sort(ar, 0, len(ar) - 1)
