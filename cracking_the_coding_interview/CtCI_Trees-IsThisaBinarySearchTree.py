# WEBSITE: HackerRank
# EXERCISE: Trees: Is This a Binary Search Tree?
# SOURCE: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree
# LANGUAGE: Python 3 

# RULES: Given the root node of a binary tree, can you determine if it's also a binary search tree?
#
# Complete the function in your editor below, which has 1 parameter: 
# a pointer to the root of a binary tree. It must return a boolean denoting whether or 
# not the binary tree is a binary search tree. You may have to write one or 
# more helper functions to complete this challenge.
#
# Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.
#
# SAMPLE INPUT: 
# (actual input is not shown on page, only diagram)
#        4
#     /    \
#   2        6
# /   \    /   \
# 1    3   5   7
#
# EXPECTED OUTPUT:
# Yes

#!/bin/python3

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

# Range of values in the BST
INT_MAX = 10000
INT_MIN = 0

# Main function being called
def check_binary_search_tree_(root):
    return (bst_helper(root, INT_MIN, INT_MAX))
 
# Helper function, return true if the given tree is a BST 
def bst_helper(node, minimum, maximum):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if this node violates min/max constraint
    if node.data < minimum or node.data > maximum:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (bst_helper(node.left, minimum, node.data - 1) and 
            bst_helper(node.right, node.data+1, maximum))
