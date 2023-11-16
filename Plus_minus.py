#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0
    negatives = 0
    zeros = 0
    
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negatives += 1
        else:
            zeros += 1
            
    total = len(arr)
    
    ratioP = positive / total
    ratioN = negatives / total
    ratioZ = zeros / total
    
    print("%.6f" % ratioP)
    print("%.6f" % ratioN)
    print("%.6f" % ratioZ)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)