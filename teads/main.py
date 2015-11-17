import sys
import math

def bfs(graph, initVertice):
    '''
    BFS algorithm over the graph gave in parameter, beginning with initialVertice. Give back the longest path for which initVertice is the first vertice.
    '''
    visit = {}
    verticeParent = {}
    for vertice in graph:
        visit[vertice] = False

    queueVisit = []
    queueVisit.append(initVertice)

    lastVerticeVisited = initVertice

    # BFS Loop
    while (len(queueVisit) > 0):

        verticeVisited = queueVisit.pop(0)
        lastVerticeVisited = verticeVisited
        verticesToVisit = graph[verticeVisited]
        visit[verticeVisited] = True

        for verticeToVisit in verticesToVisit:
            if(not(visit[verticeToVisit])):
                verticeParent[verticeToVisit] = verticeVisited
                queueVisit.append(verticeToVisit)

    # Path
    currentVertice = lastVerticeVisited
    path = []
    path.append(currentVertice)

    while  currentVertice != initVertice:
        currentVertice = verticeParent[currentVertice]
        path.append(currentVertice)

    return path




graph = {}

n = int(raw_input()) # the number of adjacency relations
for i in xrange(n):
    xi, yi = [int(j) for j in raw_input().split()]
    if(not(xi in graph)):
        graph[xi] = []
    graph[xi].append(yi)
    if(not(yi in graph)):
        graph[yi] = []
    graph[yi].append(xi)

# We detect the vertices which have only one connection
edgeVertices = []

for vertice, connectedVertices in graph.items():
    if(len(connectedVertices) == 1):
        edgeVertices.append(vertice)

# We process a BFS for the first one, we keep the longest path
# We take the last vertice in that path and process a BFS another time
# We do this until the path length doesn't change in an iteration
precPath = []
firstVertice = edgeVertices.pop(0)
while True :
    path = bfs(graph, firstVertice)
    if len(precPath) == len(path):
        precPath = path
        break
    else:
        precPath = path
        firstVertice = path[0]


# The max nb of steps to broadcast info is
print int(len(precPath)/2)
