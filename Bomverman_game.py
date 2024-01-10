#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    len_x = len(grid[0])
    len_y = len(grid)

    # Define a function to detonate the bombs
    def detonate(grid, undetonated):
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for y in range(len_y):
            for x in range(len_x):
                if grid[y][x] == 'O':
                    undetonated[y][x] = '.'
                    for dy, dx in offsets:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < len_y and 0 <= nx < len_x:
                            undetonated[ny][nx] = '.'
        return undetonated

    # Handle the case where n is 1
    if n == 1:
        return grid
    # Handle the case where n is even
    elif n % 2 == 0:
        return ['O' * len_x] * len_y
    # Handle the case where (n + 1) is divisible by 4
    elif (n) % 4 == 3:
        undet = [['O'] * len_x for _ in range(len_y)]
        grid = [list(row) for row in grid]
        grid = detonate(grid, [row[:] for row in undet])
        return [''.join(row) for row in grid]
    # Handle the case where n is odd and (n+1) not divisible by 4
    else:
        undet = [['O'] * len_x for _ in range(len_y)]
        grid = [list(row) for row in grid]
        grid = detonate(grid, [row[:] for row in undet])
        grid = detonate(grid, [row[:] for row in undet])
        return [''.join(row) for row in grid]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()