#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def leastTwo(arr):
    pair = []
    least1 = float("inf")
    least2 = float("inf")
    
    for i in arr:
        if i < least1 and i != least2:
            least1 = i
        elif i < least2:
            least2 = i
            
    pair.append(least1)
    pair.append(least2)
    return pair
    
def removeItems(items, arr):
    one, two = items[0], items[1]
    arr.remove(one)
    arr.remove(two)
    
def sweetness(one, two):
    return (one + 2 * two)

def cookies(k, A):
    
    counter = -1
    x = 0
    
    while x <= k:
        print(x)
        pair = leastTwo(A)
    
        x, two = pair[0], pair[1]
            
        removeItems(pair, A)
    
        A.append(sweetness(x, two))
        
        counter += 1
        
    
    return counter
    # Write your code here
    


def cookies(k, A):
    num_operations = 0
    A.sort()  # Initially sort the array

    while A[0] < k:
        # Check if it's possible to perform an operation
        if len(A) < 2:
            return -1  # Not enough cookies to perform an operation

        # Perform the combine operation
        least_sweet = A.pop(0)  # Remove the first element, the smallest
        second_least_sweet = A.pop(0)  # Remove the new first element, the second smallest

        # Create a new cookie and append it
        new_cookie = least_sweet + 2 * second_least_sweet
        A.append(new_cookie)

        # Sort the list again to maintain order
        A.sort()

        # Increment the operation count
        num_operations += 1

    return num_operations


def cookies(k, A):
    # Convert the list of sweetness values into a heap.
    heapq.heapify(A)
    num_operations = 0
    
    # Continue until the smallest element meets the sweetness requirement.
    while A[0] < k:
        # If we cannot combine further, return -1.
        if len(A) < 2:
            return -1
        
        # Remove the two smallest elements.
        least_sweet = heapq.heappop(A)
        second_least_sweet = heapq.heappop(A)
        
        # Combine them into a new cookie.
        new_cookie = least_sweet + 2 * second_least_sweet
        
        # Add the new cookie back to the heap.
        heapq.heappush(A, new_cookie)
        
        # Increment the count of operations.
        num_operations += 1
    
    return num_operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()