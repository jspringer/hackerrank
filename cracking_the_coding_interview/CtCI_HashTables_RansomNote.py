# WEBSITE: HackerRank
# EXERCISE: Hash Tables: Ransom Note (Cracking the Coding Interview Section)
# SOURCE: https://www.hackerrank.com/challenges/ctci-ransom-note
# LANGUAGE: Python 3 

# RULES: Given the words in the magazine and the words in the ransom note, 
# print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
# otherwise, print No.
# 
# The first line contains two space-separated integers describing the respective values 
# of m (the number of words in the magazine) and n (the number of words in the ransom note). 
# The second line contains m space-separated strings denoting the words present in the magazine. 
# The third line contains n space-separated strings denoting the words present in the ransom note.
# 
# SAMPLE INPUT: 
# 6 4
# give me one grand today night
# give one grand today
#
# EXPECTED OUTPUT:
# Yes

# Solution using a hash table as requested

#!/bin/python

def ransom_note(magazine, ransom):
    ndict = {}
    for k in magazine:
        if k in ndict:
            ndict[k] += 1
        else:
            ndict[k] = 1
    count = 0
    for item in ransom:
        if item in ndict.keys():
            value = ndict[item]
            if value > 0:
                ndict[item] -= 1
                count += 1
            else:
                break
        else:
            break
    return len(ransom) == count

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

#######################

# Simple version using Counter from Collections

# from collections import Counter

# def ransom_note(magazine, rasom):
#    return (Counter(rasom) - Counter(magazine)) == {}

# m, n = map(int, input().strip().split(' '))
# magazine = input().strip().split(' ')
# ransom = input().strip().split(' ')
# answer = ransom_note(magazine, ransom)
# if(answer):
#     print("Yes")
# else:
#     print("No")