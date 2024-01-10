#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    total_bribes = 0

    # Iterate from the end of the queue to the front
    for i in range(len(q) - 1, -1, -1):
        # Check if the current person has bribed more than two times
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        # Count how many times the current person has been bribed
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                total_bribes += 1

    print(total_bribes)



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)