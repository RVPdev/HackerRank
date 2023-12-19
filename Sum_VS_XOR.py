#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# Solution Explanation:
# The key to solving this problem lies in understanding how addition and XOR operations work at the bit level.

# Observation:

# When you add two bits, if both bits are 1, it results in a carry. However, in XOR, 1 ^ 1 = 0 without a carry.
# This means that for n + x to equal n ^ x, there must be no carry at any bit position in the addition.
# Finding x:

# The only scenario where no carry occurs during addition is when adding 0 and 1.
# Therefore, every 0 bit in n can either remain 0 or become 1 in x without causing a carry.
# Each 1 bit in n must remain 1 in x to avoid a carry (since 1 + 1 would cause a carry).
# Counting Possibilities:

# The number of valid x values depends on the number of 0 bits in n, as each 0 bit can be either 0 or 1 in x.
# If n has k zero bits, there are 2^k possible values for x.

def sumXor(n):
    # early return
    if n == 0:
        return 1
    
    # Count the number of zero bits in n
    zero_bits = bin(n).count('0') - 1  # Subtract 1 for the '0b' prefix

    # There are 2^zero_bits possibilities for x
    return 2 ** zero_bits


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()