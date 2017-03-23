# Hacker Rank
# Insertion Sort Part 1
# https://www.hackerrank.com/challenges/insertionsort1
# Python 2.7

# RULES: Given a sorted list with an unsorted number e in the rightmost cell, 
# can you write some simple code to insert e into the array so that it remains sorted?
# 
# Print the array every time a value is shifted in the array until the array is fully sorted. 
# The goal of this challenge is to follow the correct order of insertion sort.
# 
# Guideline: You can copy the value of e to a variable and consider its cell "empty". 
# Since this leaves an extra cell empty on the right, you can shift everything over 
# until V can be inserted. This will create a duplicate of each value, 
# but when you reach the right spot, you can replace it with e.
# 
# There will be two lines of input:
# Size - the size of the array
# Arr - the unsorted array of integers
# 
# On each line, output the entire array every time an item is shifted in it.
# 
# SAMPLE INPUT:
# 5
# 2 4 6 8 3
# 
# EXPECTED OUTPUT: 
# 2 4 6 8 8 
# 2 4 6 6 8 
# 2 4 4 6 8 
# 2 3 4 6 8 

#!/bin/python
def insertionSort(ar):

    currentvalue = ar[m-1]
    position = len(ar) - 1

    while ((position > 0) and (ar[position-1] > currentvalue)):
        ar[position] = ar[position-1]
        position = position-1
        currentList = " ".join(str(idx) for idx in ar)
        print currentList


    ar[position] = currentvalue
    currentList = " ".join(str(index) for index in ar)
    print currentList
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
