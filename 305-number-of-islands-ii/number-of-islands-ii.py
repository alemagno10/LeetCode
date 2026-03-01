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
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return 1

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid, res, curr = {}, [], 0
        moves = ((0,1),(0,-1),(1,0),(-1,0))
        uf = UnionFind(len(positions))

        for i, pos in enumerate(positions):
            pos = tuple(pos)
            if pos not in grid:
                grid[pos], curr = i, curr+1
                for dx, dy in moves:
                    step = (pos[0]+dx, pos[1]+dy)
                    if step in grid:
                        curr -= uf.union(i, grid[step])
            res.append(curr)
        return res


