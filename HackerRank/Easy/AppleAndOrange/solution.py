#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below


def countApplesAndOranges(s, t, a, b, apples, oranges):
    c_apples, c_oranges = 0, 0

    for i in apples:
        if a + i >= s and a + i <= t:
            c_apples += 1
    for i in oranges:
        if b + i >= s and b + i <= t:
            c_oranges += 1
    print(c_apples)
    print(c_oranges)


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
