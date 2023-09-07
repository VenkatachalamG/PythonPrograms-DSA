# Topological Sorting of DAG

class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(self.v)]

    def addEdge(self, u, v):
        self.adj[u].append(v)

    def topologicalSort(self, v, visited, stack):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.topologicalSort(i, visited, stack)
        stack.append(v)

    def TopologicalSort(self):
        stack = []
        vis = [False for i in range(self.v)]
        for i in range(self.v):
            if not vis[i]:
                self.topologicalSort(i, vis, stack)
        print(stack[::-1])


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.addEdge(4, 1)
    g.addEdge(4, 0)

    print("Following is Topological Sort of the DAG"
          " (starting from vertex 2)")
    g.TopologicalSort()
