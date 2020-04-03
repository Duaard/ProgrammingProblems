#!/bin/python3

import os


def organizingContainers(container):

    # Get the max number of possible balls in a container
    max_container = 0

    # Get the max number of balls of a certain type
    max_balls = 0

    # Cache count of each type of ball
    type_balls = [0] * len(container)

    for row in container:
        total = 0
        for i in range(len(row)):
            total += row[i]
            type_balls[i] += row[i]
            max_balls = type_balls[i] if type_balls[i] > max_balls else max_balls

        max_container = total if total > max_container else max_container

    if max_balls == max_container:
        return 'Possible'

    return 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
