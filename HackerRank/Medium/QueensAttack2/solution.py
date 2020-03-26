#!/bin/python3

import math
import os
import random
import re
import sys


def getDistance(a, b):
    # Get the distance between to points
    d = math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
    return d


def getIndex(k, c):
    # Return the index where the point b is located in respect with point a
    # 0 up, 1 up-right, 2 right... 7 up-left
    # Up
    if c[0] > k[0] and c[1] == k[1]:
        return '1, 0'
    # Up-Right
    elif c[0] > k[0] and c[1] > k[1] and abs(c[0] - k[0]) == abs(c[1] - k[1]):
        return '1, 1'
    # Right
    elif c[0] == k[0] and c[1] > k[1]:
        return '0, 1'
    # Down-Right
    elif c[0] < k[0] and c[1] > k[1] and abs(c[0] - k[0]) == abs(c[1] - k[1]):
        return '-1, 1'
    # Down
    elif c[0] < k[0] and c[1] == k[1]:
        return '-1, 0'
    # Down-Left
    elif c[0] < k[0] and c[1] < k[1] and abs(c[0] - k[0]) == abs(c[1] - k[1]):
        return '-1, -1'
    # Left
    elif c[0] == k[0] and c[1] < k[1]:
        return '0, -1'
    # Up-Left
    elif c[0] > k[0] and c[1] < k[1] and abs(c[0] - k[0]) == abs(c[1] - k[1]):
        return '1, -1'


def queensAttack(n, k, r_q, c_q, o):
    obstacles = {}

    # Initalize all possible directions, set obstacle to end of board
    # Up
    obstacles['1, 0'] = [n + 1, c_q]
    # Right
    obstacles['0, 1'] = [r_q, n + 1]
    # Down
    obstacles['-1, 0'] = [0, c_q]
    # Left
    obstacles['0, -1'] = [r_q, 0]
    # Up-Right
    tmp = min(n - r_q, n - c_q) + 1
    obstacles['1, 1'] = [r_q + tmp, c_q + tmp]
    # Down-Right
    tmp = min(r_q - 1, n - c_q) + 1
    obstacles['-1, 1'] = [r_q - tmp, c_q + tmp]
    # Down-Left
    tmp = min(r_q - 1, c_q - 1) + 1
    obstacles['-1, -1'] = [r_q - tmp, c_q - tmp]
    # Down-Right
    tmp = min(n - r_q, c_q - 1) + 1
    obstacles['1, -1'] = [r_q + tmp, c_q - tmp]

    queen = [r_q, c_q]
    print(obstacles)
    # Find the obstacles in all directions nearest to the queen
    for c in o:
        index = getIndex(queen, c)
        if index != None:
            distance_orig = getDistance(queen, obstacles[index])
            distance_new = getDistance(queen, c)
            obstacles[index] = obstacles[index] if distance_orig < distance_new else c

    # Calculate the number of squares per each direction given the nearest obstacles
    squares = 0
    # Up
    squares += obstacles['1, 0'][0] - r_q - 1
    # Right
    squares += obstacles['0, 1'][1] - c_q - 1
    # Down
    squares += r_q - obstacles['-1, 0'][0] - 1
    # Left
    squares += c_q - obstacles['0, -1'][1] - 1
    # Up-Right
    squares += min(obstacles['1, 1'][0] - r_q, obstacles['1, 1'][1] - c_q) - 1
    # Down-Right
    squares += min(r_q - obstacles['-1, 1'][0],
                   obstacles['-1, 1'][1] - c_q) - 1
    # Down-Left
    squares += min(r_q - obstacles['-1, -1'][0],
                   c_q - obstacles['-1, -1'][1]) - 1
    # Up-Left
    squares += min(obstacles['1, -1'][0] - r_q,
                   c_q - obstacles['1, -1'][1]) - 1

    return squares


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
