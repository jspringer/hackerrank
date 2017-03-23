# WEBSITE: HackerRank
# EXERCISE: Counting Sort 2
# SOURCE: https://www.hackerrank.com/challenges/countingsort2
# LANGUAGE: Python 2.7

# RULES: Create a list (array) of length equal to the number 
# range given (0-99). Count the number of times the number 
# corresponding to the index position of the list appears in 
# the original array and store that value in that index position. 
# If the value did not appear, store 0 by default. Next, 
# iterate through the count list to insert into the sorted list 
# the value corresponding to the index the number of times of 
# the value stored in the count list for the same index. 
#
# SAMPLE INPUT:
# 100
# 63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33 
# 
# EXPECTED OUTPUT: 
# 1 1 3 3 6 8 9 9 10 12 13 16 16 18 20 21 21 22 23 24 25 25 25 27 27 30 30 32 32 32 33 33 33 34 39 39 40 40 41 42 43 44 44 46 46 48 50 53 56 56 57 59 60 61 63 65 67 67 68 69 69 69 70 70 73 73 74 75 75 76 78 78 79 79 80 81 81 82 83 83 84 85 86 86 87 87 89 89 89 90 90 91 92 94 95 96 98 98 99 99 

#!/bin/python

def countSort(ar):

    countArray = [ar.count(i) for i in xrange(max(ar)+1)]
    sortedArray = []
    for i in xrange(len(countArray)):
        sortedArray += [i] * countArray[i]
    print ' '.join(map(str, sortedArray))

n = input()
ar = map(int, raw_input().strip().split(' '))
    
countSort(ar)