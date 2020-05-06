#!/bin/python3

import os


def makingAnagrams(s1, s2):
    # Find the common letters in both strings and their frequency
    letters = {}
    ans = 0
    # Record all of letters in s1 to our map
    for l in s1:
        letters[l] = 1 if l not in letters else letters[l] + 1
    # Deduct all common letters
    for l in s2:
        if l in letters:
            letters[l] -= 1
        else:
            ans += 1
    # Loop through the map to get the ans
    for l in letters:
        ans += abs(letters[l])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
