#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alpha = alpha.split()
    count = 0
    
    for c in s.lower():  # dont forget to m ake it lowercase
        for a in alpha:
            if c == a:
                count += 1
                alpha.remove(a)
                
    if count == 26:
        return "pangram"
    
    
    print(count)
    
    return "not pangram"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()