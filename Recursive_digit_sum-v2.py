#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

# def superDigit(n, k):
#     # Create the initial concatenated string by repeating `n`, `k` times
#     p = n * k
    
#     # Define the recursive function to calculate the super digit
#     def calc(p):
#         # Base case: if the length of the string `p` is 1, return it as an integer
#         if len(p) == 1:
#             return int(p)  # Make sure to return as integer
        
#         # Initialize the sum of digits
#         tempCalc = 0
        
#         # Sum up all the digits in the string `p`
#         for i in p:
#             tempCalc += int(i)
        
#         # Convert the sum back to string to feed it back to the recursive function
#         tempCalc = str(tempCalc)
        
#         # Return the result of the recursive call
#         return calc(tempCalc)  # This return is crucial for the recursion to work correctly

#     # Initial call to the recursive function with `p` where `p` is repeated `k` times.
#     # This ensures that we are starting with the correct value of `p`
#     return calc(p)  # Ensure n is treated as int then string for repetition

def superDigit(n, k):
    # Function to compute the super digit
    def getSuperDigit(x):
        if len(x) == 1:
            return x
        sum_digits = sum(int(char) for char in x)
        return getSuperDigit(str(sum_digits))
    
    # Start by summing the digits of n
    initial_sum = sum(int(char) for char in n)
    # Multiply by k to get the initial large sum
    initial_sum *= k
    
    # Get the super digit of the resulting large sum
    return getSuperDigit(str(initial_sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()