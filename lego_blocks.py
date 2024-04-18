#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Modulus for operations to prevent integer overflow and manage large numbers
    M = 10**9 + 7
    
    # lLay array to store the number of ways to build a single line (1xw) of the wall for each width w up to m
    # Initial values correspond to smaller widths where the number of combinations can be manually derived
    # lLay[1] = 1 (one block), lLay[2] = 2 (two blocks of 1 or one block of 2), and so on
    lLay = [0, 1, 2, 4, 8]
    for _ in range(5, m+1):
        # Calculate the number of layouts dynamically for widths greater than 4 using the last 4 values
        # The recurrence relation sums the last 4 values because a block can be 1, 2, 3, or 4 units wide
        lLay.append(sum(lLay[-4:]) % M)
    
    # tLay array to store the total number of configurations for an entire wall of height n and width up to m
    # This uses the power of each value in lLay to the nth power, representing stacking n rows of each layout
    tLay = [num for num in lLay]
    for i in range(m+1):
        tLay[i] = pow(lLay[i], n, M)
    
    # gLay array to store the number of "good" layouts (stable configurations without vertical cracks) for walls up to width m
    gLay = [num for num in tLay]
    for j in range(2, m+1):
        for k in range(1, j):
            # Subtract from the total configurations the number of configurations that would result in a vertical crack
            # This subtraction involves configurations where a vertical crack first appears at a column k
            # The product of the number of good layouts of width k and the total layouts of width j-k represents
            # configurations that would result in a vertical crack starting at column k
            gLay[j] -= gLay[k] * tLay[j-k]
            gLay[j] = gLay[j] % M  # Apply modulus to maintain number size
    
    # Return the number of good layouts for a wall of width m and height n
    return gLay[m]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()