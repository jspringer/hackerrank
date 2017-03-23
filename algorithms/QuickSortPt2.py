# WEBSITE: Hacker Rank
# EXERCISE: Quick Sort Part 2
# SOURCE: https://www.hackerrank.com/challenges/quicksort2
# LANGUAGE: Python 2.7

# RULES: 
# In this challenge, print your array every time your partitioning 
# method finishes, i.e. whenever two subarrays, along with 
# the pivot, are merged together.
# 
# The first element in a sub-array should be used as a pivot.
# Partition the left side before partitioning the right side.
# The pivot should be placed between sub-arrays while merging them.
# Array of length 1 or less will be considered sorted, and there 
# is no need to sort or to print them.
#
# Please maintain the original order of the elements in the left 
# and right partitions while partitioning around a pivot element.
#
# For example: Partition about the first element for the array 
# A[]={5, 8, 1, 3, 7, 9, 2} will be {1, 3, 2, 5, 8, 7, 9}
#
# There will be two lines of input:
# n - the size of the array
# ar - the n numbers of the array
# 
# SAMPLE INPUT: 
# 7
# 5 8 1 3 7 9 2
# 
# EXPECTED OUTPUT: 
# 2 3
# 1 2 3
# 7 8 9
# 1 2 3 5 7 8 9

# NOTE: They call this a quick sort but it seems more like a merge sort 
# in the way they describe it and the type of solution they are looking for. 

#!/bin/python
def partition(ar):    
   
    pivot = ar[0]
    leftArr = []
    equalArr = [pivot]
    rightArr = []
    finalArr = []
    
    if len(ar) > 1: 
       for i in range(1,len(ar)):
           if ar[i] < pivot:
              leftArr.append(ar[i])
           elif ar[i] > pivot:
              rightArr.append(ar[i])
           else:
              equalArr.append(ar[i])
    
       return partition(leftArr) + equalArr + partition(rightArr)
    finalArr = leftArr + equalArr + rightArr
    finalArrtoStr = " ".join(str(index) for index in finalArr)
    print finalArrtoStr

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)