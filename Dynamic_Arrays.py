#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Creating a list of n empty lists. Each list will serve as a dynamic array.
    arr = [[] for i in range(n)]
    lastAnswer = 0  # Initialize lastAnswer, which will be used in query type 2.
    results = []  # This will store the results of all type 2 queries.

    # Iterate through each query in the list of queries.
    for query in queries:
        q, x, y = query  # Unpack the query into its components: type (q), x, and y.

        # Calculate the index in the array list. This is done using the bitwise XOR
        # of x and lastAnswer, then taking the modulo with n.
        idx = (x ^ lastAnswer) % n
        
        # If the query type is 1, append y to the array at index idx.
        if q == 1:
            arr[idx].append(y)
        # If the query type is 2, find the value at index (y % length of arr[idx]).
        # This value becomes the new lastAnswer and is also added to the results list.
        elif q == 2:
            value = arr[idx][y % len(arr[idx])]
            results.append(value)
            lastAnswer = value

    # After processing all queries, return the results list.
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()