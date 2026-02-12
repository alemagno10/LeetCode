class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def get(m,n):
            if 0 <= m < len(grid) and 0 <= n < len(grid[0]):
                return grid[m][n]
            return 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if m == 0 and n == 0:
                    grid[m][n] = -1 if grid[m][n] == 0 else 0
                else:
                    grid[m][n] = get(m,n-1) + get(m-1,n) if grid[m][n] == 0 else 0

        return -grid[-1][-1]