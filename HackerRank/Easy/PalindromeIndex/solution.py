#!/bin/python3
import os
import math


def palindromeIndex(s):
    # Check if the world is already palindrome
    if s[:len(s)//2] == s[len(s)//2+1:]:
        return -1
    # Compare each half of s
    for i in range(len(s) // 2):
        inv = len(s) - 1 - i
        if s[i] != s[inv]:
            # Check what index to remove to make word palindrome
            # First remove index i
            cp = s[:i] + s[i+1:]
            # Get the first half of the string
            h1 = cp[:len(cp) // 2]
            # Get the second half of the string and reverse it
            h2 = cp[math.ceil(len(cp)/2):]
            h2 = h2[::-1]
            # Compare both half
            if h1 == h2:
                return i

            # Repeat same steps but for inv
            cp = s[:inv] + s[inv+1:]
            # Get the first half of the string
            h1 = cp[:len(cp) // 2]
            # Get the second half of the string and reverse it
            h2 = cp[math.ceil(len(cp)/2):]
            h2 = h2[::-1]
            # Compare both half
            if h1 == h2:
                return inv
            return -1

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
