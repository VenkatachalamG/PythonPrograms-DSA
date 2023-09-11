# Detecting bridges in a graph
from collections import defaultdict


class Graph:

    def __init__(self, vertices):
        self.v = vertices
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge(self):
        vis = [False] * self.v
        low = [999] * self.v
        disc = [999] * self.v
        p = [-1] * self.v
        for i in range(self.v):
            if not vis[i]:
                self.findBridge(i, vis, low, disc, p)

    def findBridge(self, i, vis, low, disc, p):
        vis[i] = True
        disc[i] = self.Time
        low[i] = self.Time
        self.Time += 1
        for j in self.graph[i]:
            if vis[j]:
                low[j] = min(low[j], disc[i])
            if not vis[j]:
                p[j] = i
                self.findBridge(j, vis, low, disc, p)
                low[i] = min(low[i], low[j])
                if low[j] > disc[i]:
                    print('(', i, ', ', j, ')')


g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(2, 1)
g1.addEdge(0, 3)
g1.addEdge(3, 4)
print("Bridges in first graph ")
g1.bridge()

g2 = Graph(4)
g2.addEdge(0, 1)
g2.addEdge(1, 2)
g2.addEdge(2, 3)
print("\nBridges in second graph ")
g2.bridge()

g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("\nBridges in third graph ")
g3.bridge()
