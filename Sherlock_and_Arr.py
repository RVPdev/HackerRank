#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    sum_left = 0  # Initialize the sum of elements to the left of the current element
    sum_right = sum(arr)  # Initialize the sum of all elements in the array

    for i in range(len(arr)):
        sum_right -= arr[i]  # Subtract the current element from the right sum

        if sum_left == sum_right:
            # If the sum to the left of the current element is equal to the sum
            # to the right of it, return 'YES'
            return 'YES'

        sum_left += arr[i]  # Add the current element to the left sum

    # If no such point is found where the sums are equal, return 'NO'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()