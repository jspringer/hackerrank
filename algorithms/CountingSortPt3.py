# WEBSITE: HackerRank
# EXERCISE: Counting Sort 3
# SOURCE: https://www.hackerrank.com/challenges/countingsort3
# LANGUAGE: Python 2.7

# RULES: Input contains an integer and string pair on each line 
# and the solution requested is to keep a running total of the 
# number of times all integers have appeared, increasing the 
# value in the index of the array corresponding to the number 
# that appeared. The first step is to create an array that 
# separates the integers from the strings and converts the 
# integers, which will be read as strings, to integers. Next a 
# count array is created to total the number of times each number 
# in the first array appear, the number is the index and the 
# count is stored as the value. Lastly, a series of methods are 
# applied to it within a for loop to keep a running total, 
# increasing the total count by the value in each index and 
# storing the changed total count in each index (total count 
# remains the same if the count value is 0 for an index). The 
# last method applied joins the values that have been converted 
# to strings to be printed to the console. 
#
# SAMPLE INPUT:
# 10
# 4 that
# 3 be
# 0 to
# 1 be
# 5 question
# 1 or
# 2 not
# 4 is
# 2 to
# 4 the
# 
# EXPECTED OUTPUT:
# 1 3 5 6 9 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 10 

#!/bin/python

def countSort3(ar):

   for i in xrange(n):
      ar.append(int(raw_input().strip().split(' ')[0]))
    
   count = [ar.count(i) for i in xrange(100)]
   print ' '.join([str(sum(count[:i+1])) for i in xrange(100)])

n = input()
ar = []
countSort3(ar)