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
    # Write your code here
    aplha= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    finalStr = []
    
    for i in s:
        if i.lower() in aplha:
            # identify the letter
            
            idx = aplha.index(i.lower())
            # print(idx)
            # shift by interge
            
            idx += k
            
            # replace by shifted letter
            
            if idx > 25:
                idx = idx % 26  # use modulo operator to only have a option from 1-26, nothing more 
            # append to final list
            # finalStr.append(aplha[idx])
            
            # check if lower or upper case
            if i.isupper():
                finalStr.append(aplha[idx].upper())
            else:
                finalStr.append(aplha[idx])
                
        else:
            finalStr.append(i)
    
    
    print(finalStr)
    
    return "".join(finalStr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()