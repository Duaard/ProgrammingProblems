#!/bin/python3

import os


def sherlockAndAnagrams(s):
    # Store in map the frequency of each substring
    n = len(s)
    mp = {}

    for i in range(n):
        # Reset each substring every i loop
        sb = ''
        # Loop through j to get all possible substring for index i
        for j in range(i, n):
            # print(f'j: {j}')
            # Build substring by adding index j
            # Sort to make sure each sb is unique
            sb = ''.join(sorted(sb + s[j]))
            # Add this substring to our map
            mp[sb] = mp.get(sb, 0)
            # Increment frequency
            mp[sb] += 1

    ans = 0
    # Get the ans by looping through the map
    # formula for getting anagrams based on permutation
    for k, v in mp.items():
        ans += (v*(v-1))//2
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
