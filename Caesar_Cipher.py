#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    result = ""

    for char in s:
        if char.isalpha():
            # Determine the starting point (A for uppercase, a for lowercase)
            start = ord('A') if char.isupper() else ord('a')

            # Shift the character and wrap around using modulo operation
            shifted = chr(start + (ord(char) - start + k) % 26)
            result += shifted
        else:
            # Non-alphabetic characters remain unchanged
            result += char

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()