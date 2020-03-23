#!/bin/python3

import os


def isNotCompatible(arr, a, b):
    if b in arr[a]:
        return True
    return False


def nonDivisibleSubset(k, s):

    # Create a dict of remainders for each s[i]
    r_map = {}

    for i in s:
        r = i % k
        if r_map.get(r) is None:
            r_map[r] = 1
        else:
            r_map[r] += 1
    print(r_map)
    done = []
    subset = 0
    for i, val in r_map.items():
        if i not in done:
            # This pair hasn't been tested yet
            a = i
            b = k - i
            if a == 0:
                # There can only be one for this val
                subset += 1
            elif a == b:
                # There can only be one for this val
                subset += 1
            elif b not in r_map:
                # There's no val in set not compatible with this
                subset += r_map[a]
            else:
                if r_map[a] > r_map[b]:
                    subset += r_map[a]
                elif r_map[a] < r_map[b]:
                    subset += r_map[b]
                else:
                    subset += r_map[a]
                done.extend([a, b])

    return subset


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
