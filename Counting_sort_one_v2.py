
import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def countingSort(arr):
#     # Write your code here
#     freq = []
    
#     maximum = max(arr)
    
#     # print(maximum)
    
#     for i in range(maximum + 1):
#         # print(i)
#         counter = 0
#         for j in arr:
#             if i == j:
#                 counter += 1
        
#         freq.append(counter)
    
#     return(freq)

def countingSort(arr):
    frequency = [0] * 100
    
    for num in arr:
        frequency[num] += 1
    
    return frequency

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()