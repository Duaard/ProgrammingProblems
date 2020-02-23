#!/bin/python3

import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    # Store how many games we bought
    games = 0
    # While the price isn't minimum
    while(p > m and s >= p):
        games += 1
        s -= p
        p -= d

    if p <= m:
        # Divide the min price to remaning cash
        games += s // m

    return games


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
