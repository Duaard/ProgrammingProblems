#!/bin/python3

import os


def absolutePermutation(n, k):

    avail_num = [i for i in range(n + 1)]
    p = []

    # Loop through i
    for i in range(1, n + 1):
        tmp = None
        # Get the smallest possible number that would result in k as differece
        if i - k > 0:
            # The i is bigger than k
            # Check if it is still available
            if avail_num[i - k] == i - k:
                tmp = i - k
                # Make this num not avail
                avail_num[i - k] = 0

        # If smallest is not possible
        if tmp == None:
            # Check if i + k is within range
            if i + k <= n:
                # Check if the second least is available
                if avail_num[i + k] == i + k:
                    tmp = i + k
                    # Make this num not avail
                    avail_num[i + k] = 0

        # No numbers are avail
        if tmp == None:
            return [-1]
        else:
            p.append(tmp)

    return p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
