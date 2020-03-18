#!/bin/python3


def quick_sort(ar, n):
    # Performs a quick sort using divide and conquer

    # Base case, array is already sorted if n is 1
    if n <= 1:
        return ar

    # Get the pivot element
    pivot = ar[0]

    # Sort the ar using the pivot element
    left, right = [], []
    for i in ar:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)

    # Perform quick sort on the sub arrays
    left = quick_sort(left, len(left))
    right = quick_sort(right, len(right))

    # Combine the sorted arr
    sorted_ar = left + [pivot] + right
    [print(i, end=' ') for i in sorted_ar]
    print()
    return sorted_ar


# Get the size of array
n = int(input())
# Get the array
ar = list(map(int, input().split()))

quick_sort(ar, n)
