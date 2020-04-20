#!/bin/python3
import os


def marsExploration(s):
    # Loop through the array and count how many letters were changed
    changed = 0
    for i, c in enumerate(s):
        if i % 3 == 0 or i % 3 == 2:
            # Must be S
            changed = changed + 1 if c != 'S' else changed
        else:
            # Must be O
            changed = changed + 1 if c != 'O' else changed

    return changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
