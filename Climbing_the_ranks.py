#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     res = []
    
#     for r in player:
#         # print(r)
#         ranked.append(r)
#         ranked = list(set(ranked))
#         ranked.sort(reverse=True)
        
#         print(ranked.index(r) + 1)
#         res.append(ranked.index(r) + 1)
        
#     return res

def climbingLeaderboard(ranked, player):
    # Remove duplicates from the ranked list and sort it in descending order
    unique_ranked = sorted(list(set(ranked)), reverse=True)
    ranks = []  # This list will store the ranks for each player's score
    index = len(unique_ranked) - 1  # Start from the end of the unique ranked list

    for score in player:
        # Iterate through each score in the player's list of scores

        # Move down the unique_ranked list until the player's score is less than or equal to the ranked score
        while index >= 0 and score >= unique_ranked[index]:
            index -= 1  # Decrement index to move down the leaderboard

        # Append the player's rank to the ranks list
        # The rank is the current index + 2 because of 0-based indexing and because the player's rank is one more than the index
        ranks.append(index + 2)

    return ranks  # Return the list of ranks for each player's score


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()