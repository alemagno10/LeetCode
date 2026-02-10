class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def inBound(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def dfs(x,y):
            if not inBound(x,y) or grid[x][y] == 0:
                return 0

            res, grid[x][y] = 0,0
            for dx, dy in moves:
                res += dfs(x+dx, y+dy)
            return 1+res
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(i,j))
        return res