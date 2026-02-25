from collections import deque

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        cache = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        res = 0

        def get(i,j):
            return cache[i][j] if i >= 0 and j >= 0 else 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    cache[i][j] = 1 + min(get(i-1,j), get(i,j-1), get(i-1,j-1))    
                    res = max(res, cache[i][j]**2) 

        return res 