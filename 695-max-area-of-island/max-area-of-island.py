class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        maxArea = 0

        def dfs(x,y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return 0
            
            if grid[x][y] == 0:
                return 0
            
            area = 1
            grid[x][y] = 0

            for m,n in moves:
                area += dfs(x+m, y+n)
            return area
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                maxArea = max(maxArea, dfs(x,y))

        return maxArea
        
