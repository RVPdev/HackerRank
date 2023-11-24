#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    result = 0 # initialize a result varialbe 
    
    for idx, i in enumerate(s): # iterate over the array
        upperEnd = idx + m # set an upper boundary for your array section
        
        if upperEnd > len(s): # if the array ends break the loop
            break
        
        if sum(s[idx:upperEnd]) == d: # use idx and upper end to section the array and use the sum method to sum sections
            result += 1
    
    total = sum(s[0:3])
    
            
    print(total)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()