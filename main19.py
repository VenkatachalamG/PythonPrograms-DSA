# Implementation of disjoint set by path compression and union by rank

class Disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):

        if self.parent[x] is not x:
            self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep == yrep:
            return

        if self.rank[xrep] < self.rank[yrep]:
            self.parent[xrep] = yrep
        elif self.rank[xrep] > self.rank[yrep]:
            self.parent[yrep] = xrep

        else:
            self.parent[xrep] = yrep
            self.rank[xrep] = self.rank[xrep] + 1


obj = Disjoint(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)
if obj.find(4) == obj.find(0):
    print('Yes')
else:
    print('No')
if obj.find(1) == obj.find(0):
    print('Yes')
else:
    print('No')
