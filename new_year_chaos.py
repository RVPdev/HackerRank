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

    # Inner loop: Check each person who could have bribed the person at position i
    for i in range(len(q) - 1, -1, -1):
        # Check if the current person has bribed more than two times
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        # Count how many times the current person has been bribed
        for j in range(max(0, q[i] - 2), i):
            # max(0, q[i] - 2): Calculate the original position of the person at i, then go two positions back.
            # This is because a person can only move forward by bribing up to two people.
            # The max ensures we don't go to a negative index.

            # Check if the person at position j (who was originally behind i) has a larger number.
            # A larger number indicates they were originally further back in the queue and have moved ahead of i by bribing.
            if q[j] > q[i]:
                total_bribes += 1

    print(total_bribes)



if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)