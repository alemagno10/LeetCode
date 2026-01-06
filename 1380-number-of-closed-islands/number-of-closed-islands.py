class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = 0

        def isValid(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])

        def dfs(x,y):
            if not isValid(x,y):
                return False
            if grid[x][y]:
                return True
            
            grid[x][y] = 1
            return min([dfs(a+x, b+y) for a,b in directions])

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if not grid[x][y]:
                    islands += int(dfs(x,y))
        return islands