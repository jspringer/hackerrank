# WEBSITE: HackerRank
# EXERCISE: Sorting: Bubble Sort (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-bubble-sort
# LANGUAGE: Python 3 

# RULES: Given an -element array of distinct elements, 
# sort array in ascending order using the Bubble Sort algorithm. 
# Once sorted, print the following three lines:

# Array is sorted in numberOfSwaps swaps.
# First Element: firstElement, the first element in the sorted array.
# Last Element: lastElement, the last element in the sorted array.
#
# SAMPLE INPUT:
# 3
# 3 2 1
#
# EXPECTED OUTPUT: 
# Array is sorted in 3 swaps.
# First Element: 1
# Last Element: 3

#!/bin/python3

def bubble_sort_swap_count(n, a):
    numberOfSwaps = 0
    for i in range(n): 
        # Track number of elements swapped during a single array traversal

        for j in range(n - 1): 
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                a[j + 1], a[j] = a[j], a[j + 1]
                numberOfSwaps += 1

    # Extra space is not added in the strings since Python automatically adds space before and after variable
    print("Array is sorted in", numberOfSwaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[n-1])

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
bubble_sort_swap_count(n, a)