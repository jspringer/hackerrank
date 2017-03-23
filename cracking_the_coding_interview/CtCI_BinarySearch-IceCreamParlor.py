# WEBSITE: HackerRank
# EXERCISE: Binary Search: Ice Cream Parlor (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-ice-cream-parlor
# LANGUAGE: Python 3 

# RULES: Given the value of m and the cost of each flavor for t trips to the Ice Cream Parlor, 
# help Sunny and Johnny choose two distinct flavors such that they spend their entire pool of money (m) during each visit. 
# For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase 
# as two space-separated integers on a new line. 
# You must print the smaller ID first and the larger ID second.
# 
# Problem name suggests a binary search approach is expected.
# However, this fits the TWO SUM problem, best real world approach is to use hashmap for O(n). 
# See: https://leetcode.com/articles/two-sum/
#
# SAMPLE INPUT:
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
#
# EXPECTED OUTPUT: 
# 1 4
# 1 2

#!/bin/python3

def pick_ice_creams(costs, money_remaining, num_flavors, start_money):
    
    if (money_remaining <= 0) or (len(costs) == num_flavors - 2):
        return []

    elif len(costs) == num_flavors - 1:
        for i, cost in enumerate(costs):
            if cost == money_remaining:
                return [(cost, i+2)] #Recursive stack, at depth of 1, position is offset by 1
        return []

    for i, cost in enumerate(costs):
        if len(costs) == num_flavors:
            next_pick = pick_ice_creams(costs[:i] + costs[i+1:], money_remaining - cost, num_flavors, start_money)
            if len(next_pick) == 0:
                continue
            combination = [(cost, i+1)] + next_pick
            return combination
               
def solve(costs, money_remaining, num_flavors, start_money):
    cost_position_list = pick_ice_creams(costs, money_remaining, num_flavors, start_money)
    l = [p[1] for p in cost_position_list]
    l.sort()
    print(' '.join(map(str,l)))

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    solve(a, m, n, m)


# Faster, simpler hashmap approach

#!/bin/python3

# t = int(input().strip())
# for a0 in range(t):
#     m = int(input().strip())
#     n = int(input().strip())
#     a = list(map(int, input().strip().split(' ')))
#     flavors = {}
#     for i, flavor in enumerate(a): 
#         if (m - flavor) in flavors:
#             print("{} {}".format(flavors[(m - flavor)]+1, i+1))
#         else:
#             flavors[flavor] = i