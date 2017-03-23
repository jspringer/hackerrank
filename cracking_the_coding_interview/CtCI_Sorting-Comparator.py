# WEBSITE: HackerRank
# EXERCISE: Sorting: Comparator (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-comparator-sorting
# LANGUAGE: Python 3 

# RULES: Given an array of n Player objects, write a comparator that sorts them in order of decreasing score; 
# if 2 or more players have the same score, sort those players alphabetically by name. 

# SAMPLE INPUT:
# 5
# amy 100
# david 100
# heraldo 50
# aakansha 75
# aleksa 150
#
# EXPECTED OUTPUT: 
# aleksa 150
# amy 100
# david 100
# aakansha 75
# heraldo 50

#!/bin/python3

from functools import cmp_to_key

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        print("%s %s" %(self.name, self.score))

    def comparator(a, b):
        if a.score == b.score:
            if sorted([a.name, b.name]) == [a.name, b.name]:
                return -1
            else:
                return 1
        else:
            return b.score - a.score

n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)
    
data = sorted(data, key=cmp_to_key(Player.comparator))
for i in data:
    print(i.name, i.score)