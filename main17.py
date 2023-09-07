# BFS Traversal of a Graph
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, v):
        vis = [False] * (len(self.graph) + 1)
        gq = []
        gq.append(v)
        vis[v] = True
        while gq:
            p = gq.pop(0)
            print(p, end=' ')
            for i in self.graph[v]:
                if not vis[i]:
                    gq.append(i)
                    vis[i] = True


if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(2, 1)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)
