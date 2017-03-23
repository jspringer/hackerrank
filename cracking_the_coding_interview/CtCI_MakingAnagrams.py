# WEBSITE: HackerRank
# EXERCISE: Strings: Making Anagrams (Cracking the Coding Interview Section)
# SOURCE: https://www.hackerrank.com/challenges/ctci-making-anagrams
# LANGUAGE: Python 3 

# RULES: Given two strings, a and b, that may or may not be of the same length,
# determine the minimum number of character deletions required to make a and b anagrams. 
# Any characters can be deleted from either of the strings.
# 
# SAMPLE INPUT: 
# cde
# abc
#
# EXPECTED OUTPUT:
# 4

#!/bin/python3

def number_needed(a, b):
    
    # combine values in both lists into one dictionary, no duplicates
    anagram_dict = dict.fromkeys(a + b, 0) 
    
    # count (value) for each letter (key) that is in list a is increased by 1 (1 max)
    for letter in a:
        anagram_dict[letter] += 1 

    # count (value) for each letter (key) that is in list a is decreased by 1 (-1 max)
    for letter in b:
        anagram_dict[letter] -= 1 

    # absolute value of counts for all letters are added (sum) and returned
    return sum([abs(val) for val in anagram_dict.values()]) 

a = input().strip()
b = input().strip()

print(number_needed(a, b))
