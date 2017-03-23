# WEBSITE: Hacker Rank
# EXERCISE: Quick Sort Part 1
# SOURCE: https://www.hackerrank.com/challenges/quicksort1
# LANGUAGE: Python 2.7

# RULES: 
# Given ar and p = ar[0], partition ar into left, right, and equal 
# using the Divide instructions above. Then print each element in 
# left followed by each element in equal, followed by each element 
# in right on a single line. Your output should be space-separated.
# 
# There is no need to sort the elements in-place; you can create 
# two lists and stitch them together at the end.
# 
# The first line contains n (the size of ar). 
# The second line contains n space-separated integers describing ar 
# (the unsorted array). The first integer (corresponding to ar[0]) is 
# your pivot element, p.
#
# NOTE: They call this a quick sort but it seems more like a merge sort 
# in the way they describe it and the type of solution they are looking for. 
# Also, like other exercises in this section, they request unusual solutions 
# that implement an algorithm, or part of it, rather than the algorithm itself 
# returning a single solution. 

#!/bin/python

def partition(ar):    
   
    pivot = ar[0]
    leftArr = []
    equalArr = [pivot]
    rightArr = []
    finalArr = []
    
    for i in range(1,len(ar)):
        if ar[i] < pivot:
            leftArr.append(ar[i])
        elif ar[i] > pivot:
            rightArr.append(ar[i])
        else:
            equalArr.append(ar[i])
    
    finalArr = leftArr + equalArr + rightArr
    finalArrtoStr = " ".join(str(index) for index in finalArr)
    print finalArrtoStr

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
