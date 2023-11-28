#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

def sockMerchant(n, ar):
    # Sort the array to group identical elements together
    ar.sort()

    # Use groupby to group identical elements and create sublists
    # Each sublist contains all occurrences of a particular sock type
    pairs = [list(group) for key, group in groupby(ar)]
    
    # Initialize a counter for the number of pairs
    nOfPairs = 0
    
    # Print the grouped socks for debugging or verification
    print(pairs)
    
    # Iterate through each group of socks
    for a in pairs:
        # For each type of sock, count how many pairs can be formed
        # This is done by dividing the count of each sock type by 2
        # and taking the integer part (// operator)
        nOfPairs += len(a) // 2
    
    # Return the total number of pairs
    return nOfPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the total number of socks (not used in this implementation)
    n = int(input().strip())

    # Read the array of socks, where each number represents a type of sock
    ar = list(map(int, input().rstrip().split()))

    # Call the sockMerchant function and store the result
    result = sockMerchant(n, ar)

    # Write the result to the output file
    fptr.write(str(result) + '\n')

    fptr.close()
