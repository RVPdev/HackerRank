#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def leftDiagonal(arr):
    total = 0
    for idx, a in enumerate(arr):
        total += a[idx]
        
    return total
    
def rightDiagonal(arr):
    total = 0
    length = len(arr) -1
    
    for a in arr:
        total += a[length]
        length -= 1
    
    return total
        

def diagonalDifference(arr):
    # Write your code here
    leftD = leftDiagonal(arr)
    rightD = rightDiagonal(arr)
    
    result = abs(leftD - rightD)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()