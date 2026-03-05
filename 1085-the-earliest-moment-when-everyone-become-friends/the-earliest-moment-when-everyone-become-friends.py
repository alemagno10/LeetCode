class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return 0
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += p2
        else:
            self.par[p1] = p2
            self.rank[p2] += p1
        return 1

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort()

        for time, x1, x2 in logs:
            n -= uf.union(x1,x2)
            if n == 1:
                return time
        return -1
        