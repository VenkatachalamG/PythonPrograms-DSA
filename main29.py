# Checking for a cycle in a graph
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.v = vertices

    def add(self, u, v):
        self.graph[u].append(v)

    def isCyclic(self):
        visited = [False] * (self.v + 1)
        recursion = [False] * (self.v + 1)
        for i in range(self.v):
            if visited[i] is False:
                self.aCycle(i, visited, recursion)
            else:
                return True

    def aCycle(self, v, visited, recursion):
        visited[v] = 1
        recursion[v] = 1
        for i in self.graph[v]:
            if not visited[i]:
                if self.aCycle(i, visited, recursion):
                    return True
            else:
                recursion[i] = True
                return True
        recursion[v] = False
        return False


if __name__ == '__main__':
    g = Graph(4)
    g.add(0, 1)
    g.add(0, 2)
    g.add(1, 2)
    g.add(2, 0)
    g.add(2, 3)
    g.add(3, 3)

    if g.isCyclic() == 1:
        print('Graph has a cycle')
    else:
        print('Graph has no  cycle')
