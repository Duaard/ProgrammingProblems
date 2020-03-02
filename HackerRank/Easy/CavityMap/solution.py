#!/bin/python3

import math
import os
import random
import re
import sys


def cavityMap(grid):
    cavity_map = []
    # Loop through each cell
    for row in range(len(grid)):
        tmp_row = ''
        for col in range(len(grid)):
            cell = grid[row][col]
            # Check if the cell is not at the border
            if row != 0 and col != 0 and row != len(grid) - 1 and col != len(grid) - 1:
                # Check if it's edges are lower in depth

                # Vertical edges
                if int(cell) > int(grid[row - 1][col]) and int(cell) > int(grid[row + 1][col]):
                    # Horizontal edges
                    if int(cell) > int(grid[row][col - 1]) and int(cell) > int(grid[row][col + 1]):
                        cell = 'X'
            # Add the modified cell
            tmp_row += cell
        # Add the row placeholder
        cavity_map.append(tmp_row)
    return cavity_map


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
