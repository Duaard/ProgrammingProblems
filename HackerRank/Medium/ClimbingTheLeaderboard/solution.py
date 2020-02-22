#!/bin/python3

import math
import os
import random
import re
import sys


class Leaderboard:
    ranking_score = {}
    score_ranking = {}
    last_rank = 1

    def __init__(self, scores):
        for score in scores:
            # Populate ranking
            if self.score_ranking.get(score) is None:
                rank = self.last_rank
                self.score_ranking[score] = rank
                self.ranking_score[rank] = score
                self.last_rank += 1

    # Binary search using dictionary
    def binarySearchDict(self, score, ranking, start, end):
        # Do a binary search to look for rank
        i = start + math.ceil((end - start) / 2)
        if score > ranking[i]:
            # Check if the score is greater than this i and less than i-1
            if i != start and score < ranking[i-1]:
                # This is the rank
                return i
            elif i == start:
                # This score is the first rank in this subset
                return i
            else:
                # Look for it again in the left part of the ranking
                return self.binarySearchDict(score, ranking, start, i - 1)
        elif score < ranking[i]:
            # Check if the score is less than this i and greater than i + 1
            if i != end and score > ranking[i + 1]:
                # Current ranking[i] rank is i + 1
                return i + 1
            # Check if this score is the least rank
            elif i == end:
                # Rank is the new least
                return end + 1
            else:
                # Look for it again but subset the list and add offset rank
                return self.binarySearchDict(score, ranking, i + 1, end)
        else:
            # The values are equal, this is the rank of the score
            return i


def climbingLeaderboard(scores, alice):
    # Create a leader board
    leaderboard = Leaderboard(scores)
    alice_ranking = []
    last_rank = 0
    for score in alice:
        if len(alice_ranking) == 0:
            # This is the initial ranking
            rank = leaderboard.binarySearchDict(
                score, leaderboard.ranking_score, 1, len(leaderboard.score_ranking))
        else:
            rank = leaderboard.binarySearchDict(
                score, leaderboard.ranking_score, 1, last_rank - 1)
        last_rank = rank
        alice_ranking.append(rank)
    return alice_ranking


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
