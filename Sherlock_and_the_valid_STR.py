#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    cnt = Counter(s)        # Count the frequency of each character in the string
    cnt2 = Counter(cnt.values())  # Count the frequency of each frequency

    # If there's only one type of frequency, the string is valid
    if len(cnt2) == 1:
        return "YES"

    # If there are more than two types of frequencies, the string is not valid
    if len(cnt2) > 2:
        return "NO"

    # Extract the two frequency keys
    key1, key2 = cnt2.keys()

    # Check if one of the frequencies occurs only once
    if cnt2[key1] == 1 or cnt2[key2] == 1:
        # Check if the difference between the two frequencies is 1
        # (which means we can remove one character to make the string valid)
        if abs(key1 - key2) == 1:
            return "YES"
        
        # Check if one of the frequencies is 1 and occurs only once
        # (which means we can remove the character with this frequency to make the string valid)
        if 1 in cnt2.keys():
            if cnt2[1] == 1:
                return "YES"

    # If none of the above conditions are met, the string is not valid
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
