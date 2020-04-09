#!/bin/python3

import os


def nearbyBomb(row, col, grid):
    # Check if this cell has a neighboring bomb
    if row + 1 < len(grid) and grid[row + 1][col] == 'O':
        return True
    if row - 1 >= 0 and grid[row - 1][col] == 'O':
        return True
    if col + 1 < len(grid[0]) and grid[row][col + 1] == 'O':
        return True
    if col - 1 >= 0 and grid[row][col - 1] == 'O':
        return True
    return False

# Complete the bomberMan function below.


def bomberMan(n, grid):
    rows = len(grid)
    cols = len(grid[0])
    mod = n % 4

    if n == 1:
        # Initial state
        return grid

    if mod == 2 or mod == 0:
        # All cells are filled with bombs
        return ['O' * cols for i in range(rows)]

    # Get the exploded state of grid
    exploded = []
    # Exploded bomb state
    for row in range(rows):
        new_row = []
        for col in range(cols):
            # Check if there's a bomb within four adjacent cells
            if nearbyBomb(row, col, grid):
                val = '.'
            else:
                # Invert the value of the cell
                val = 'O' if grid[row][col] == '.' else '.'
            new_row.append(val)
        exploded.append("".join(new_row))

    if mod == 1:
        # Explode the exploded state
        new_grid = []
        # Exploded bomb state
        for row in range(rows):
            new_row = []
            for col in range(cols):
                # Check if there's a bomb within four adjacent cells
                if nearbyBomb(row, col, exploded):
                    val = '.'
                else:
                    # Invert the value of the cell
                    val = 'O' if exploded[row][col] == '.' else '.'
                new_row.append(val)
            new_grid.append("".join(new_row))
        return new_grid

    elif mod == 3:
        # Exploded state
        return exploded


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
