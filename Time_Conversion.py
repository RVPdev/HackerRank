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
    
    formatedStr = ""
    
    if "PM" in s:
        if s[0:2] == "12":
            formatedStr = s[0: -2]
        else:
            tHour = int(s[0:2]) + 12
            x = s.strip(s[0:2])
            formatedStr = str(tHour) + x[0:-2]
        
    if "AM" in s:
        if s[0:2] == "12":
            x = s.strip(s[0:2])
            formatedStr = "00" + x[0:-2]
        else:
            formatedStr = s[0: -2]
        
        
    return formatedStr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()