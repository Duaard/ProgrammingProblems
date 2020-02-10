#!/bin/python3

import math
import os


def repeatedString(s, n):
    # Get the a occurence in the original string
    a_count = s.count('a')
    # If there is no a return the count
    if a_count == 0:
        return a_count
    extra_a = 0
    # Loop for the remainder to get the extra_a
    for i in range(n % len(s)):
        if s[i] == 'a':
            extra_a += 1
    # Get the final value of a_count by multiplying
    # it by the quotient of len(s) and n
    a_count *= math.floor(n / len(s))
    a_count += extra_a

    return a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3


# Complete the repeatedString function below.

def repeatedString(s, n):
    # Get the a occurence in the original string
    a_count = s.count('a')
    # If there is no a return the count
    if a_count == 0:
        return a_count
    extra_a = 0
    # Loop for the remainder to get the extra_a
    for i in range(n % len(s)):
        if s[i] == 'a':
            extra_a += 1
    # Get the final value of a_count by multiplying
    # it by the quotient of len(s) and n
    a_count *= math.floor(n / len(s))
    a_count += extra_a

    return a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
