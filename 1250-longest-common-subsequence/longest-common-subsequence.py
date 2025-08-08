class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0

            key = (i,j)
            if key in memo:
                return memo[key]

            if text1[i] == text2[j]:
                memo[key] = 1 + dfs(i+1, j+1)
            else:
                memo[key] = max(dfs(i, j+1), dfs(i+1, j))
            return memo[key] 

        return dfs(0,0) 