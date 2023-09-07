# Hamiltonian Cycle
class Graph:
    def __init__(self, n):
        self.graph = [0 for row in range(n) for col in range(n)]
        self.n = n

    def isCycle(self, path, pos, vertex):
        if self.graph[path[pos - 1]][vertex] == 0:
            return False
        for v in path:
            if vertex == v:
                return False
        return True

    def isHam(self, path, pos):
        if pos == self.n:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            else:
                return False
        for v in range(1, self.n):
            if self.isCycle(path, pos, v):
                path[pos] = v
                if self.isHam(path, pos + 1):
                    return True
                path[pos] = -1
        return False

    def hamCycle(self):
        path = [-1] * self.n
        path[0] = 0
        if self.isHam(path, 1) is False:
            print('No hamiltonian Cycle')
            return False
        self.display(path)
        return True

    def display(self, path):
        for v in path:
            print(v, end=' ')
        print(path[0])


g1 = Graph(5)
g1.graph = [[0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 1, 0, 0, 1], [0, 1, 1, 1, 0]]
g1.hamCycle()

g2 = Graph(5)
g2.graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 0]]
g2.hamCycle()
