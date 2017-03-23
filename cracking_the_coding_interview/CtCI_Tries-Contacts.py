# WEBSITE: HackerRank
# EXERCISE: Tries: Contacts (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-contacts
# LANGUAGE: Python 3 

# RULES: Find and print the number of contact names beginning with letters following each ’find’ keyword. 
# Use trie data structure
# Name and partial contain lowercase English letters only.
# The input doesn't have any duplicate name for the add operation.
#
# SAMPLE INPUT:
# 4
# add hack
# add hackerrank
# find hac
# find hak 
#
# EXPECTED OUTPUT: 
# 2
# 0

#!/bin/python3

class Node(object):
    def __init__(self, letters=None):
        self.letters = letters
        self.children = {}
        self.count = 1

    def expand(self):
        if not self.letters:
            return
        self.children[self.letters[0]] = Node(self.letters[1:])
        self.letters = None


class Trie(object):
    def __init__(self):
        self.root = Node()

    def add_contact(self, contact):
        node = self.root
        for i in range(len(contact)):
            letter = contact[i]
            if letter not in node.children:
                new_node = Node(letters=contact[i + 1:])
                node.children[letter] = new_node
                break
            else:
                node = node.children[letter]
                node.expand()
                node.count += 1

    def get_count(self, contact):
        node = self.root
        for letter in contact:
            if letter not in node.children:
                return 0
            node = node.children[letter]
            node.expand()
        return node.count
                
        
n = int(input().strip())
trie = Trie()
for _ in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add_contact(contact)
    else:
        print(trie.get_count(contact))

#################
# Alternative (naive) solution that does not implement a trie, but keeps count of specific strings using a dictionary
#
# n = int(input().strip())
# 
# names = {}
# 
# for a0 in range(n):
#     op, contact = input().strip().split(' ')
# 
#     if op == "add":
#         for i in range(1,len(contact)+1):
#             sub = contact[0:i]
#             if sub in names:
#                 names[sub] += 1
#             else:
#                 names.update({sub:1})
#         
#     elif op == "find":
#         if contact in names:
#             print(names[contact])
#         else:
#             print(0)

