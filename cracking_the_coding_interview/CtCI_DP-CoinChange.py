# WEBSITE: HackerRank
# EXERCISE: DP: Coin Change (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-coin-change
# LANGUAGE: Python 3 

# RULES: Given a number of dollars, n, and a list of dollar values for m distinct coins, 
# C = {c0, c1, c2,…, cm-1}, find and print the number of different ways you can make change 
# for n dollars if each coin is available in an infinite quantity.
#
# The first line contain two space-separated integers describing the respective values of n and m. 
# The second line contains m space-separated integers describing the respective values of c0, c1, c2,…, cm-1, 
# where each integer denotes the dollar value of a distinct coin available in an infinite quantity.
#
# Print a single integer denoting the number of ways we can make change for n dollars 
# using an infinite supply of our m types of coins.
#
# SAMPLE INPUT:
# 4 3
# 1 2 3 
#
# EXPECTED OUTPUT: 
# 4

# Solution below uses the Integer Partition Algorithm: 
# https://en.wikipedia.org/wiki/Partition_(number_theory)
# https://www.youtube.com/watch?v=ZaVM057DuzE

#!/bin/python3

import sys

def make_change(coins, n):
    results = [0 for _ in range(n + 1)]
    results[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
    return results[n]

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))

