# Kruskal's Algorithm

class Graph:
    def __init__(self, v):
        self.graph = []
        self.v = v

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[y] < rank[x]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        parent = []
        rank = []
        result = []
        e = 0
        i = 0
        self.graph = sorted(self.graph, key=lambda it: it[2])

        for v in range(self.v):
            parent.append(v)
            rank.append(0)

        while e < self.v - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minCost = 0
        for u, v, wt in result:
            minCost += wt
            print("%d -- %d == %d" % (u, v, wt))
        print("Minimum Cost :", minCost)


if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    # Function call
    g.KruskalMST()
