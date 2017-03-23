# WEBSITE: Hacker Rank
# EXERCISE: Running Time of Algorithms
# SOURCE: https://www.hackerrank.com/challenges/runningtime
# LANGUAGE: Python 2.7

# RULES: Can you modify your previous Insertion Sort implementation 
# to keep track of the number of shifts it makes while sorting? 
# The only thing you should print is the number of shifts made by 
# the algorithm to completely sort the array. A shift occurs when 
# an element's position changes in the array. 
# Do not shift an element if it is not necessary.
# 
# The first line contains N, the number of elements to be sorted. 
# The next line contains N integers a[1], a[2], ..., a[N].
#
# Output the number of shifts it takes to sort the array.
# 
# SAMPLE INPUT: 
# 5
# 2 1 3 1 2
# 
# EXPECTED OUTPUT:
# 4

#!/bin/python

def insertionSort(ar):
    
    totalShifts = 0

    for index in range(1,len(ar)):
        currentvalue = ar[index]
        position = index

        while ((position > 0) and (ar[position-1] > currentvalue)):
            ar[position] = ar[position-1]
            totalShifts += 1
            position = position-1

        ar[position] = currentvalue

    print totalShifts 

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)