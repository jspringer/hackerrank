# WEBSITE: Hacker Rank
# EXERCISE: Insertion Sort Part 2
# SOURCE: https://www.hackerrank.com/challenges/insertionsort2
# LANGUAGE: Python 2.7

# RULES: Print the array after each iteration of the insertion-sort, 
# i.e., whenever the next element is placed at its correct position.
# 
# Since the array composed of just the first element is already "sorted", 
# begin printing from the second element and on.
# 
# There will be two lines of input:
# s - the size of the array
# ar - a list of numbers that makes up the array
#
# SAMPLE INPUT: 
# 6
# 1 4 3 5 6 2
# 
# EXPECTED OUTPUT
# 1 4 3 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 2 3 4 5 6 

#!/bin/python

def insertionSort(ar):

    for index in range(1,len(ar)):
        currentvalue = ar[index]
        position = index

        while ((position > 0) and (ar[position-1] > currentvalue)):
            ar[position] = ar[position-1]
            position = position-1

        ar[position] = currentvalue
        currentList = " ".join(str(indx) for indx in ar)
        print currentList
    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)