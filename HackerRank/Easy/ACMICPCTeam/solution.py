#!/bin/python3

import math
import os
import random
import re
import sys


def acmTeam(topic):
    topic_max = 0
    topic_perm = 0
    # Loop through all permutations
    for i in range(len(topic)-1):
        for j in range(i + 1, len(topic)):
            # Add the two topics
            combined_str = str(int(topic[i]) + int(topic[j]))
            # Count the 0
            count_0 = combined_str.count('0')
            # The number of 1 is total - total number of 0
            counter = len(topic) - (count_0 + (len(topic) - len(combined_str)))
            if counter > topic_max:
                # New Max
                topic_max = counter
                topic_perm = 1
            elif counter == topic_max:
                # New pern, sane nax
                topic_perm += 1

    return [topic_max, topic_perm]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
