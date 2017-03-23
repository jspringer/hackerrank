# WEBSITE: HackerRank
# EXERCISE: Stacks: Balanced Brackets (Cracking the Coding Interview Section)
# SOURCE: https://www.hackerrank.com/challenges/ctci-balanced-brackets
# LANGUAGE: Python 3 

# RULES: Given  strings of brackets, determine whether each sequence of brackets is balanced. 
# If a string is balanced, print YES on a new line; otherwise, print NO on a new line.
# 
# The first line contains a single integer, n, denoting the number of strings. 
# Each line i of the n subsequent lines consists of a single string, s, 
# denoting a sequence of brackets.
#
# SAMPLE INPUT:
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}
#
# EXPECTED OUTPUT: 
# YES
# NO
# YES


# Dictionary and stack solution

#!/bin/python3

def is_matched(expression):
    pairs = {'{' : '}', '[' : ']', '(' : ')'}
    stack = []
    for bracket in expression:
        if bracket in pairs:
            # adds right bracket in pairs dictionary (left bracket is key) to stack
            stack.append(pairs[bracket]) 
        # after going through brackets in pairs, checks to see if right brackets in stack match up in correct order
        elif not stack or bracket != stack.pop(): 
            return False

    # Stack should be empty at this point, so should return True
    return not stack 

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")


# No dictionary solution. Doesn’t use stack though as instructions requested.

# def is_matched(expression):
#     while( len(expression) > 0):
#         initialExp = expression
#         expression = expression.replace('()','')
#         expression = expression.replace('{}','')
#         expression = expression.replace('[]','')
#         if initialExp == expression:
#     		return False
        
#     return True

# t = int(input().strip())
# for a0 in range(t):
#     expression = input().strip()
#     if is_matched(expression) == True:
#         print("YES")
#     else:
#         print("NO")