# WEBSITE: HackerRank
# EXERCISE: Recursion: Fibonacci Numbers (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-fibonacci-numbers
# LANGUAGE: Python 3 

# RULES: Given n, complete the fibonacci function so it returns fibonacci(n).
# 
# The first line contains an integer, p, denoting the number of integers to check for primality. 
# Each of the  subsequent lines contains an integer, n, you must test for primality.

# SAMPLE INPUT:
# 3
#
# EXPECTED OUTPUT: 
# 2

#!/bin/python3

memo = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in memo.keys():
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

