# WEBSITE: HackerRank
# EXERCISE: BFS: Shortest Reach in a Graph (Cracking the Coding Interview)
# SOURCE: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach
# LANGUAGE: Python 3 

# RULES: Given q queries in the form of a graph and some starting node, s, 
# perform each query by calculating the shortest distance from starting node s to all the other nodes in the graph. 
# Then print a single line of n - 1 space-separated integers listing node s’s shortest distance 
# to each of the n - 1 other nodes (ordered sequentially by node number); 
# if s is disconnected from a node, print -1 as the distance to that node.
#
# The first line contains two space-separated integers describing the respective values of n (the number of nodes) 
# and m (the number of edges) in the graph.
# Each line i of the m subsequent lines contains two space-separated integers, u and v, 
# describing an edge connecting node u to node v.
# The last line contains a single integer, s, denoting the index of the starting node.
#
# Consider an undirected graph consisting of n nodes where each node is labeled from 1 to n 
# and the edge between any two nodes is always of length 6. 
# We define node s to be the starting position for a BFS.
# 
# For each of the q queries, print a single line of n - 1 space-separated integers 
# denoting the shortest distances to each of the n - 1 other nodes from starting position s. 
# These distances should be listed sequentially by node number (i.e., 1, 2, …, n), 
# but should not include node s. If some node is unreachable from s, 
# print -1 as the distance to that node.
# 
# SAMPLE INPUT:
# 2
# 4 2
# 1 2
# 1 3
# 1
# 3 1
# 2 3
# 2
#
# EXPECTED OUTPUT: 
# 6 6 -1
# -1 6

#!/bin/python3

import queue 
from collections import defaultdict

class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        q = queue.Queue()

        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)

        distances.pop(root)

        print(' '.join(map(str,distances)))

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)
