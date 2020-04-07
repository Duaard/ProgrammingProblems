#!/bin/python3

import os


def surfaceArea(A):
    # Get the total surface area given a 2D array of values
    sa = 0

    # The surface area of top and bottom remains the same
    # in respect with the rows and columns
    row = len(A)
    col = len(A[0])
    sa += row * col * 2

    # Surface area of opposite sides will be the same
    # Find the surface area of each side in respect with row and col
    sa_row, sa_col = 0, 0
    for c in range(col):
        for r in range(row):
            # Get the height of this cell
            h = A[r][c]

            # The last row of cells will always show regardless
            if r + 1 == row:
                # Get the full sa of this cell
                sa_row += h
            else:
                # Get the sa of the cell that won't be blocked by the next row
                if h > A[r+1][c]:
                    sa_row += h - A[r+1][c]

            # The last col of cells will always show regardless
            if c + 1 == col:
                # Get the full sa of this cell
                sa_col += h
            else:
                # Get the sa of the cell that won't be blocked by the next col
                if h > A[r][c+1]:
                    sa_col += h - A[r][c+1]

    sa += (sa_row * 2) + (sa_col * 2)
    return sa


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
