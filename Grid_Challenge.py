#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

# def gridChallenge(grid):
#     # Write your code here
#     sortedGrid = []
    
#     vertical = [""] * len(grid)
    
#     counter = 0
    
    
#     for i in grid:
#         sortedGrid.append("".join(sorted(i)))
        
#     for i in range(len(grid)):
#         vertical[0] += sortedGrid[i][0]
#         vertical[1] += sortedGrid[i][1]
#         vertical[2] += sortedGrid[i][2]
#         vertical[3] += sortedGrid[i][3]
#         vertical[4] += sortedGrid[i][4]
        
#     print(vertical)
    
#     for i in vertical:
#         if (i == "".join(sorted(i))):
#             counter += 1
#         else:
#             return "NO"

#     return "YES"
    
def gridChallenge(grid):
    # Sort each row of the grid
    sortedGrid = ["".join(sorted(row)) for row in grid]

    # Number of columns in the grid
    num_columns = len(sortedGrid[0])

    # Check each column to ensure it is sorted
    for col in range(num_columns):
        for row in range(1, len(sortedGrid)):
            if sortedGrid[row][col] < sortedGrid[row - 1][col]:
                return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()