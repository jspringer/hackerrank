# WEBSITE: Hacker Rank
# EXERCISE: Quick Sort Part 3
# SOURCE: https://www.hackerrank.com/challenges/quicksort3
# LANGUAGE: Python 2.7

# RULES: Instead of copying the array into multiple sub-arrays, 
# use indices to keep track of the different sub-arrays. You 
# can pass the indices to a modified partition method. The 
# partition method should partition the sub-array and then 
# return the index location where the pivot gets placed, so you 
# can then call partition on each side of the pivot.
# 
# > Always select the last element in the 'sub-array' as a pivot.
# > Partition the left side and then the right side of the sub-array.
# > Print out the whole array at the end of every partitioning method.
# > An array of length 1 or less will be considered sorted, and 
# there is no need to sort or to print them.
#
# Since you cannot just create new sub-arrays for the elements, 
# partition method will need to use another trick to keep track of 
# which elements are greater and which are lower than the pivot.
# 
# The In-place Trick (Lomuto Partitioning)
# If an element is lower than the pivot, you should swap it with 
# a larger element on the left-side of the sub-array.
# Greater elements should remain where they are.
# At the end of the partitioning method, the pivot should be swapped 
# with the first element of the right partition, consisting of all 
# larger elements, of the sub-array.
# To ensure that you don't swap a small element with another small 
# element, use an index to keep track of the small elements that 
# have already been swapped into their "place".
#
# There will be two lines of input:
# n - the size of the array
# ar - the  numbers of the array
#
# SAMPLE INPUT: 
# 7
# 1 3 9 8 2 7 5
# 
# EXPECTED OUTPUT: 
# 1 3 2 5 9 7 8
# 1 2 3 5 9 7 8
# 1 2 3 5 7 8 9

# NOTE: They call this a quick sort using Lomuto Partitioning. 
# Also, like other exercises in this section, they request unusual solutions 
# that implement an algorithm, or part of it, rather than the algorithm itself 
# returning a single solution. 

#!/bin/python

def qsort_lomuto(ar, start, end):
    # base case
    if end - start <= 0:
        return ar

    pivot = ar[end]
    index = start
    
    # loop less final value (pivot)
    for i in xrange(start, end):
        if ar[i] <= pivot:
            ar[i],ar[index] = ar[index],ar[i]
            index += 1

    ar[index],ar[end] = ar[end],ar[index]
    print ' '.join(str(x) for x in ar)
    # left side
    ar = qsort_lomuto(ar,start,index-1)
    
    # right side
    ar = qsort_lomuto(ar,index+1,end)
    return ar

n = int(raw_input())
ar = [int(x) for x in raw_input().split()]
    
qsort_lomuto(ar, 0, n-1)