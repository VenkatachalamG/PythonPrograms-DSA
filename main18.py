# DFS Traversal of graph

from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(self.v)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def DFS(self, v):
        vis = [False for i in range(self.v)]
        gq = []
        gq.append(v)
        while len(gq):
            q = gq[-1]
            gq.pop()

            if not vis[q]:
                print(q, end=' ')
                vis[q] = True

            for i in self.adj[v]:
                if not vis[i]:
                    gq.append(i)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 3)
    g.addEdge(2, 1)
    g.addEdge(2, 0)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.DFS(2)
