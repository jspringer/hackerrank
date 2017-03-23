# WEBSITE: HackerRank
# EXERCISE: Bit Manipulation: Lonely Integer (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-lonely-integer
# LANGUAGE: Python 3 

# RULES: Consider an array of n integers, A = [a0, a1, …, an-1], 
# where all but one of the integers occur in pairs. In other words, 
# every element in A occurs exactly twice except for one unique element.
#
# Given A, find and print the unique element.
#
# The first line contains a single integer, n, denoting the number of integers in the array. 
# The second line contains n space-separated integers describing the respective values in A.
#
# SAMPLE INPUT:
# 3
# 1 1 2
#
# EXPECTED OUTPUT: 
# 2


#!/bin/python3

import sys

def lonely_integer(num_arr):
    result = 0
    for num in num_arr:
        result ^= num

    return result

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))