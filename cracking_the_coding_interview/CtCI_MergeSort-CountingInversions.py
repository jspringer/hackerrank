# WEBSITE: HackerRank
# EXERCISE: Merge Sort: Counting Inversions (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-merge-sort
# LANGUAGE: Python 3 

# RULES: Given d datasets, print the number of inversions that must be swapped to sort each dataset on a new line.

# SAMPLE INPUT:
# 2  
# 5  
# 1 1 1 2 2  
# 5  
# 2 1 3 1 2
#
# EXPECTED OUTPUT: 
# 0
# 4

#!/bin/python3

MAX_ARR_INT = 10**8

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftArr = arr[0:mid]
        rightArr = arr[mid:]
        merged = merge(merge_sort(leftArr), merge_sort(rightArr))
        return merged
    else:
        return arr

def merge(leftArr, rightArr):
    global count
    newLeftArr = leftArr + [MAX_ARR_INT]
    newRightArr = rightArr + [MAX_ARR_INT]
    mergedArr = []
    i, j = 0, 0
    for _ in range(len(leftArr) + len(rightArr)):
        # Add the value in index j of the right array to the merged array if it is greater than i in left
        # Increase the inversion swap count
        # Increase the right index counter j
        if newLeftArr[i] > newRightArr[j]:
            mergedArr += [newRightArr[j]]
            j += 1
            count += len(leftArr) - i
        # Add the value in index i of the left array to the merged array
        # Increase the right index counter i
        else:
            mergedArr += [newLeftArr[i]]
            i += 1
    return mergedArr

def count_inversions(arr):
    global count
    count = 0
    merge_sort(arr)
    return count

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))


