#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    stair = n - 1
    for h in range(n):
        for i in range(n):
            if i >= stair:
                print('#', end = '')
            else:
                print(' ', end = '')
        print('')
        stair -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
