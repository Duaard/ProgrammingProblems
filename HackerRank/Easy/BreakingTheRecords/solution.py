#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    maxScore = minScore = scores[0]
    maxCount = minCount = 0
    for score in scores:
        if score > maxScore:
            maxScore = score
            maxCount += 1
        if score < minScore:
            minScore = score
            minCount += 1
    return [maxCount, minCount]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
