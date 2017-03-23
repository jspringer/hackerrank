# WEBSITE: HackerRank
# EXERCISE: Linked Lists: Detect a Cycle (Cracking the Coding Interview Section)
# SOURCE: https://www.hackerrank.com/challenges/ctci-linked-list-cycle
# LANGUAGE: Python 3 

# RULES: It has one parameter: a pointer to a Node object named head 
# that points to the head of a linked list. 
# Your function must return a boolean denoting whether or not there is a cycle in the list. 
# If there is a cycle, return true; otherwise, return false.
# The hidden code checker prints to stdout 0 if false and 1 if true.
# 
# SAMPLE INPUT: 
# {node: 1, next: None}
# 
# EXPECTED OUTPUT: 
# 0
#
# SAMPLE INPUT: 
# {node: 1, next: 2} {node: 2, next: 3} {node: 3, next: 2}
# 
# EXPECTED OUTPUT: 
# 1

# Solution below is based on the fact there is a constraint

#!/bin/python3

def has_cycle(head):
    node = head
    for i in in range(100):
        if node is None:
            return False
        node = node.next
    return True

# If a constraint is not given in the problem, this code can be used instead

# def has_cycle(head):
#     fast = head
#     slow = head
#     try:
#         slow = slow.next
#         fast = fast.next.next
#         if slow == fast:
#             return True
#     except:
#         return False