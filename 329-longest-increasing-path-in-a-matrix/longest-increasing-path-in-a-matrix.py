class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = [[0]*len(matrix[0]) for i in range(len(matrix))]

        def isInside(i,j):
            return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

        def dfs(i,j):
            if memo[i][j]:
                return memo[i][j]

            path = 1
            for x,y in [(0,1),(1,0),(-1,0),(0,-1)]:
                x,y = x+i, y+j
                if isInside(x,y) and matrix[i][j] < matrix[x][y]:
                    path = max(path, 1+dfs(x,y))
            
            memo[i][j] = path
            return path

        lgst = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lgst = max(lgst, dfs(i,j))
        
        return lgst