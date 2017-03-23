# WEBSITE: HackerRank
# EXERCISE: Time Complexity: Primality (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-big-o
# LANGUAGE: Python 3 

# RULES: Given p integers, determine the primality of each integer 
# and print whether it is Prime or Not prime on a new line.
# 
# The first line contains an integer, p, denoting the number of integers to check for primality. 
# Each of the  subsequent lines contains an integer, n, you must test for primality.

# SAMPLE INPUT:
# 3
# 12
# 5
# 7
#
# EXPECTED OUTPUT: 
# Not prime
# Prime
# Prime

#!/bin/python3

from math import sqrt

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    counter = 0
    for i in range(2,int(sqrt(n))+1):
        if (n % i == 0):
            counter += 1
    if (counter > 0 or n < 2):
        print("Not prime")
    else:
        print("Prime")
