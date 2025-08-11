class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        
        def dfs(i,j):
            if i+j == len(s3):
                return i == len(s1) and j == len(s2)
            
            key, k = (i,j), i+j
            if key in memo:
                return memo[key]
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res |= dfs(i+1, j)

            if j < len(s2) and s2[j] == s3[k]:
                res |= dfs(i, j+1)
            
            memo[key] = res
            return res
        
        return dfs(0,0)