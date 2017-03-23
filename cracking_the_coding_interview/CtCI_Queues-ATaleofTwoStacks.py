# WEBSITE: HackerRank
# EXERCISE: Queues: A Tale of Two Stacks (Cracking the Coding Interview Section)
# SOURCE: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
# LANGUAGE: Python 3 

# RULES: In this challenge, you must first implement a queue using two stacks. 
# Then process  queries, where each query is one of the following  types:
# 1. Enqueue element x into the end of the queue.
# 2. Dequeue the element at the front of the queue.
# 3. Print the element at the front of the queue.
# 
# The first line contains a single integer, q, denoting the number of queries. 
# Each line i of the q subsequent lines contains a single query in the form described 
# in the problem statement above. All three queries start with an integer denoting 
# the query type, but only query 1 is followed by an additional space-separated value, x, 
# denoting the value to be enqueued.
# 
# SAMPLE INPUT:
# 10
# 1 42
# 2
# 1 14
# 3
# 1 28
# 3
# 1 60
# 1 78
# 2
# 2
# 
# EXPECTED OUTPUT: 
# 14
# 14

#!/bin/python3

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.last = []
    
    def adjustStack(self):
        if not self.first:
            while self.last:
                self.first.append(self.last.pop())
                
    def peek(self):
        return self.first[-1] if self.first else self.last[0]                
                        
    def pop(self):
        self.adjustStack()
        self.first.pop()                
        
    def put(self, value):
        self.last.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())