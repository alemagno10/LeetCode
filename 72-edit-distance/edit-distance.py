class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        
        def dfs(i,j):
            if len(word1) == i and len(word2) == j:
                return 0
            
            key = (i,j)
            if key in memo:
                return memo[key]
            
            if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                return dfs(i+1, j+1)
            
            distance = math.inf
            if i < len(word1) and j < len(word2):
                distance = min(distance, 1+dfs(i+1, j+1))
            if i < len(word1):
                distance = min(distance, 1+dfs(i+1, j))
            if j < len(word2):
                distance = min(distance, 1+dfs(i, j+1))
            
            memo[key] = distance
            return distance
        
        return dfs(0,0)