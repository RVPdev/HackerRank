#!/bin/python3

import math
import os
import random
import re
import sys


def isBalanced(s):
    # Initialize a list to use as a stack to store the opening brackets.
    arr_in = []
    
    # String containing all types of opening brackets.
    entryBrackets = "{[("
    
    # Dictionary to map each closing bracket to its corresponding opening bracket.
    exitBrackets = {"}": "{", "]": "[", ")": "("}
    
    # Iterate through each character in the input string.
    for i in s:
        # Check if the character is an opening bracket.
        if i in entryBrackets:
            # If it is, push it onto the stack.
            arr_in.append(i)
        else:
            # If it is a closing bracket, check if the stack is empty.
            if len(arr_in) == 0:
                # If the stack is empty, there is no matching opening bracket.
                return "NO"
            # Check if the top of the stack matches the expected opening bracket.
            elif arr_in[-1] == exitBrackets[i]:
                # If it matches, pop the top of the stack.
                arr_in.pop(-1)
            else:
                # If it doesn't match, the brackets are not balanced.
                return "NO"
    # Check if the stack is empty after processing all brackets.
    if arr_in:
        # If the stack is not empty, some opening brackets didn't have matching closing brackets.
        return "NO"
    
    # If the stack is empty, all brackets matched correctly.
    return "YES"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
