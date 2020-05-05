#!/bin/python3

import os


def anagram(s):
    # Odd len makes it impossible to form an anagram
    if len(s) % 2 != 0:
        return -1

    # Divide the string into 2 and count how many chars doesnt have a pair
    m = {}
    ans = 0
    for i in range(len(s)):
        l = s[i]
        if i < len(s) // 2:
            m[l] = 1 if l not in m else m[l] + 1
        else:
            if l in m:
                m[l] -= 1
    for l in m:
        if m[l] > 0:
            ans += m[l]
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
