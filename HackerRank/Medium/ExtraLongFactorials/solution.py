#!/bin/python3

import math
import os
import random
import re
import sys


def factorial(n):
    # Factorials can be solved recursively
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def extraLongFactorials(n):
    print(factorial(n))


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
