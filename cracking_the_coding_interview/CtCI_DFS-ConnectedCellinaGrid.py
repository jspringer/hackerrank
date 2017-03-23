# WEBSITE: HackerRank
# EXERCISE: DFS: Connected Cell in a Grid (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid
# LANGUAGE: Python 3 

# RULES: Given an  matrix, find and print the number of cells in the largest region in the matrix. 
# Note that there may be more than one region in the matrix.
#
# Consider a matrix with n rows and m columns, where each cell contains either a 0 or a 1 
# and any cell containing a 1 is called a filled cell. Two cells are said to be connected 
# if they are adjacent to each other horizontally, vertically, or diagonally; 
# in other words, cell [i][j] is connected to cells [i - 1][j - 1], [i - 1][j], [i - 1[j + 1], 
# [i][j - 1], [i][j + 1], [i + 1][j - 1], [i + 1][j], and [i + 1][j + 1], 
# provided that the location exists in the matrix for that [i][j].
#
# X X 0 0     1 1 0 0
# 0 X X 0     0 1 1 0
# 0 0 X 0     0 0 1 0
# 1 0 0 0     X 0 0 0
# The first region has five cells and the second region has one cell. 
# Because we want to print the number of cells in the largest region of the matrix, we print .
# 
# SAMPLE INPUT:
# 4
# 4
# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0
#
# EXPECTED OUTPUT: 
# 5

#!/bin/python3

def getBiggestRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion
            
def countCells(grid, i, j):
    if (not(i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == 0):
        return 0
    count = 1
    grid[i][j] = 0
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    count += countCells(grid, i + 1, j + 1)
    count += countCells(grid, i - 1, j - 1)
    count += countCells(grid, i - 1, j + 1)
    count += countCells(grid, i + 1, j - 1)
    return count