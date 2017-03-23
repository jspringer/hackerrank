# WEBSITE: HackerRank
# EXERCISE: Recursion: Davis' Staircase (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-recursive-staircase
# LANGUAGE: Python 3 

# RULES: Davis has s staircases in his house 
# and he likes to climb each staircase 1, 2, or 3 steps at a time. 
#
# Given the respective heights for each of the  staircases in his house, 
# find and print the number of ways he can climb each staircase on a new line.
# 
# The first line contains a single integer, s, denoting the number of staircases in his house. 
# Each line i of the s subsequent lines contains a single integer, n, 
# denoting the height of staircase i.

# SAMPLE INPUT:
# 3
# 1
# 3
# 7
#
# EXPECTED OUTPUT: 
# 1
# 4
# 44

#!/bin/python3

def num_of_ways_to_climb(staircase_height, steps_at_a_time, memo={}):
    if staircase_height < 0:
        return 0
    if staircase_height == 0:
        return 1
    # Memoization to reduce time
    if memo.get(staircase_height):
        return memo[staircase_height]
    total = 0
    for step in steps_at_a_time:
        total += num_of_ways_to_climb((staircase_height - step), steps_at_a_time, memo)
    memo[staircase_height] = total
    return total


a = [1, 2, 3] # Number of steps that can be taken at a time
s = int(input().strip())
for _ in range(s):
    n = int(input().strip())
    print(num_of_ways_to_climb(n, a))
