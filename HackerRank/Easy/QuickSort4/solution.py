#!/bin/python3


def insertion_sort(arr):
    # Record the number of shifts performed
    shifts = 0
    # Loop through each element in arr starting from arr[1]
    for elem in range(1, len(arr)):
        # Save the current indexed val
        val = arr[elem]
        # Loop through the array starting from elem index to 0
        for i in range(elem, -1, -1):
            # val is greater than equal the next val
            if arr[i-1] <= val or i == 0:
                arr[i] = val
            # else val is still lower, copy the next val to current index
            else:
                arr[i] = arr[i-1]
                # Record shift
                shifts += 1

            # If the current index is the place of val
            if (arr[i] == val):
                # Stop the loop
                break

    # Return the number of shifts
    return shifts


def quick_sort(ar, lo, hi, shift):
    if lo < hi:
        [i, shift] = partition(ar, lo, hi, shift)
        # Sort the left sub array
        shift = quick_sort(ar, lo, i - 1, shift)
        # Sort the right sub array
        shift = quick_sort(ar, i + 1, hi, shift)
    return shift


def partition(ar, lo, hi, shift):
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
            # Shift occured
            shift += 1

    # Put the pivot in the right place by swapping
    # it's pos and the current i
    tmp = ar[i]
    ar[i] = pivot
    ar[hi] = tmp
    shift += 1

    # The ar is now partitioned
    # Return the partitioned arr and pos of i
    return [i, shift]


# Get the size of array
n = int(input())
# Get the array
ar = list(map(int, input().split()))

insertion_shift = insertion_sort(ar.copy())
quick_shift = quick_sort(ar.copy(), 0, len(ar) - 1, 0)
print(insertion_shift - quick_shift)
