#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[:2])
    meridian = s[-2:]
        
    if hour == 12:
        hour = 0 if meridian == "AM" else 12
    elif meridian == "PM":
        hour += 12
    
    return f'{hour:02d}{s[2:-2]}'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()