# WEBSITE: HackerRank
# EXERCISE: Heaps: Find the Running Median (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-find-the-running-median
# LANGUAGE: Python 3 

# RULES: The median of a dataset of integers is the midpoint value of the dataset 
# for which an equal number of integers are less than and greater than the value. 
# To find the median, you must first sort your dataset of integers in 
# non-decreasing order, then:
# 1. If your dataset contains an odd number of elements, the median is the 
# middle element of the sorted sample. In the sorted dataset {1, 2, 3}, 2 is the median.
# 2. If your dataset contains an even number of elements, the median is the average 
# of the two middle elements of the sorted sample. In the sorted dataset {1, 2, 3, 4}, 
# (2+3)/2 = 2.5 is the median.
#
# Given an input stream of  integers, you must perform the following task for each  integer:
# 1. Add the ith integer to a running list of integers.
# 2. Find the median of the updated list (i.e., for the first element through the ith element).
# 3. Print the list's updated median on a new line. The printed value must be a 
# double-precision number scaled to 1 decimal place (i.e., 12.3 format).
# 
# The first line contains a single integer, n, denoting the number of integers in the data stream. 
# Each line i of the n subsequent lines contains an integer, ai, to be added to your list.
# 
# SAMPLE INPUT: 
# 6
# 12
# 4
# 5
# 3
# 8
# 7
# 
# EXPECTED OUTPUT: 
# 12.0
# 8.0
# 5.0
# 4.5
# 5.0
# 6.0

#!/bin/python3

import sys

from heapq import heappush, heappop

class MinHeap:
    def __init__(self): self.h = []
    def push(self, val): heappush(self.h, val)
    def pop(self): return heappop(self.h)
    def peek(self): return self.h[0]
    def __len__(self): return len(self.h)
    
class MaxHeap:
    def __init__(self): self.h = []
    def push(self, val): heappush(self.h, -val)
    def pop(self): return -(heappop(self.h))
    def peek(self): return -(self.h[0])
    def __len__(self): return len(self.h)

def balance_heaps(min_heap, max_heap):
    if len(max_heap) < len(min_heap):
        max_heap.push(min_heap.pop())
    elif len(max_heap) > len(min_heap) + 1: 
        min_heap.push(max_heap.pop())
        
def current_median(n, min_heap, max_heap):
    if len(max_heap) > 0 and n > max_heap.peek():
        min_heap.push(n)
    else:
        max_heap.push(n)
    balance_heaps(min_heap, max_heap) 
    if len(max_heap) == len(min_heap):
        return (max_heap.peek() + min_heap.peek()) / 2
    return max_heap.peek()
            
def running_median(a):
    if len(a) == 0: return
    max_heap = MaxHeap()
    min_heap = MinHeap()
    for n in a:
        print("%.1f" % current_median(n, min_heap, max_heap))

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)

running_median(a)