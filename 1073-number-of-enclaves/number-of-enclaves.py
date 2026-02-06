class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        def offBoundary(x,y):
            return not(0 <= x < ROWS and 0 <= y < COLS)

        def dfs(x,y):
            if offBoundary(x,y) or grid[x][y] == 0:
                return 0

            grid[x][y] = 0
            res = 0
            for dx, dy in moves:
                res += dfs(dx+x, dy+y)
            return 1+res
        
        for i in range(ROWS):
            dfs(i,0)
            dfs(i,COLS-1)
        for j in range(COLS):
            dfs(0,j)
            dfs(ROWS-1,j)
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res += dfs(i,j)
        return res