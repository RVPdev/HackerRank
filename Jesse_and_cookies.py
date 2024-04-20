#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def leastTwo(arr):
    pair = []
    least1 = float("inf")
    least2 = float("inf")
    
    for i in arr:
        if i < least1 and i != least2:
            least1 = i
        elif i < least2:
            least2 = i
            
    pair.append(least1)
    pair.append(least2)
    return pair
    
def removeItems(items, arr):
    one, two = items[0], items[1]
    arr.remove(one)
    arr.remove(two)
    
def sweetness(one, two):
    return (one + 2 * two)

def cookies(k, A):
    
    counter = -1
    x = 0
    
    while x <= k:
        print(x)
        pair = leastTwo(A)
    
        x, two = pair[0], pair[1]
            
        removeItems(pair, A)
    
        A.append(sweetness(x, two))
        
        counter += 1
        
    
    return counter
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()