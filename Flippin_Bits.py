
import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Convert to binary and remove the '0b' prefix
    binary_str = bin(n)[2:]

    # Pad the binary string to 32 bits
    binary_str = binary_str.rjust(32, '0')

    # Flip the bits
    flipped_str = ''.join('1' if bit == '0' else '0' for bit in binary_str)

    # Convert back to integer
    return int(flipped_str, 2)

# One Liner
# def flippingBits(n):
#     # Flip the bits with bitwise NOT (~)
#     # Use bitwise AND with 0xFFFFFFFF to limit to 32 bits
#     return ~n & 0xFFFFFFFF


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())
    # 01111111111111111111111111111111
    # 00000000000000000000000000000001
    # 00000000000000000000000000000000

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()