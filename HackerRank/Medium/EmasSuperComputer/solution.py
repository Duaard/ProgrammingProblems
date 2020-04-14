#!/bin/python3

import os


def getArea(row, col, grid):
    # Gets the area of a cell in respect with the grid
    d = 1
    valid = True
    # Check it's four directions until it breaks
    while(valid):
        if row + d >= len(grid) or row - d < 0 or col + d >= len(grid[0]) or col - d < 0:
            # Out of range
            valid = False
        elif grid[row+d][col] == 'B' or grid[row-d][col] == 'B' or grid[row][col+d] == 'B' or grid[row][col-d] == 'B':
            # Bad cell
            valid = False
        else:
            # Possible to extend this plus
            d += 1
    a = (d - 1) * 4 + 1
    return a


def overlap(r1, c1, r2, c2, a1, a2):
    # Checks if two plusses overlaps with each other
    l1 = int((a1 - 1) / 4)
    l2 = int((a2 - 1) / 4)
    cells1 = [[r1, c1]]
    cells2 = [[r2, c2]]

    for i in range(l1):
        # Get the cell in left
        cells1.append([r1, c1 - (i * 1 + 1)])
        # Up
        cells1.append([r1 - (i * 1 + 1), c1])
        # Right
        cells1.append([r1, c1 + (i * 1 + 1)])
        # Down
        cells1.append([r1 + (i * 1 + 1), c1])

    for i in range(l2):
        # Get the cell in left
        cells2.append([r2, c2 - (i * 1 + 1)])
        # Up
        cells2.append([r2 - (i * 1 + 1), c2])
        # Right
        cells2.append([r2, c2 + (i * 1 + 1)])
        # Down
        cells2.append([r2 + (i * 1 + 1), c2])

    # Check if the two cells has the same value
    for cell in cells1:
        if cell in cells2:
            return True

    return False


def possibleAreas(max_area):
    # Returns the list of possible areas given the max_area
    areas = []
    for i in range(((max_area - 1) // 4) + 1):
        areas.append((i * 4) + 1)
    return areas


def twoPluses(grid):
    rows = len(grid)
    cols = len(grid[0])
    area = [[0] * cols for i in range(rows)]
    m1, m2 = 0, 0

    # Loop through each cell and calculate it's area
    for row in range(rows):
        for col in range(cols):
            # Check if it's a good cell
            if grid[row][col] == 'G':
                # Calculate it's area
                a = getArea(row, col, grid)
                area[row][col] = a
                if a > m1:
                    m2 = m1
                    m1 = a
                elif a == m1 or a > m2:
                    m2 = a
    # Find the maximum product
    max_p = 0
    for r1 in range(rows):
        for c1 in range(cols):
            # Look for the c that yield max product with this cell
            for r2 in range(rows):
                for c2 in range(cols):
                    if r1 != r2 or c1 != c2:
                        # Check if these cells overlap
                        if not overlap(r1, c1, r2, c2, area[r1][c1], area[r2][c2]):
                            p = area[r1][c1] * area[r2][c2]
                            if p > max_p:
                                max_p = p
                        else:
                            # Starting from the least possible area, increase each area accordingly to get max_p
                            for a1 in possibleAreas(area[r1][c1]):
                                for a2 in possibleAreas(area[r2][c2]):
                                    if not overlap(r1, c1, r2, c2, a1, a2):
                                        p = a1 * a2
                                        if p > max_p:
                                            max_p = p

    return max_p


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
