#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Calculate the sum of the digits of n and multiply it by k
    res = sum(int(c) for c in str(n)) * k

    # Check if the result is greater than 9 (i.e., not a single digit)
    if res > 9:
        # If res is not a single digit, call superDigit recursively with the new sum
        return superDigit(str(res), 1)
    else:
        # If res is a single digit, return it as the super digit
        return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()