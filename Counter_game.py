#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

def counterGame(n):
    # Subtract 1 from n and convert it to binary
    setbits = bin(n-1).count("1")
    
    # Count the number of set bits (1s) in the binary representation
    if setbits % 2 == 1:
        # If the number of set bits is odd, Louise wins
        return "Louise"
    else:
        # If the number of set bits is even, Richard wins
        return "Richard"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
