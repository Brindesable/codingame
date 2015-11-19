import sys
import math

def dfs(graph, d, v):

    if len(graph[v]) == 0:
        # if the vertice has no children
        d[v] = 1
    else:
        # else we compute the length for each child vertice, we take the greater + 1
        maxChildLength = 0
        for vChild in graph[v]:
            d = dfs(graph, d, vChild)
            if d[vChild] > maxChildLength:
                maxChildLength = d[vChild]

        d[v] = maxChildLength + 1

    return d

# oriented acyclic graph
graph = {}
# associate each vertice with the size of the longest chain beginning with this vertice
d = {}

n = int(raw_input()) # the number of adjacency relations
for i in xrange(n):
    xi, yi = [int(j) for j in raw_input().split()]

    if(not(xi in graph)):
        graph[xi] = []
    graph[xi].append(yi)
    if(not(yi in graph)):
        graph[yi] = []

    if(not(xi in d)):
        d[xi] = None
    if(not(yi in d)):
        d[yi] = None

maxLength = 0
for v in d:
    if d[v] is None:
        d = dfs(graph, d, v)
        if(d[v] > maxLength):
            maxLength = d[v]

print (maxLength)