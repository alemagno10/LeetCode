from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, x1):
        if self.par[x1] != x1:
            self.par[x1] = self.find(self.par[x1])
        return self.par[x1]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return 0
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        return 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        mapper = {}

        for i,acc in enumerate(accounts):
            for email in acc[1:]: 
                if email in mapper:
                    uf.union(i, mapper[email])
                else:
                    mapper[email] = i

        aux = defaultdict(list)
        for k,v in mapper.items():
            aux[uf.find(v)].append(k)
        
        res = []
        for k,v in aux.items():
            res.append([accounts[uf.find(k)][0]] + sorted(v))
        
        return res