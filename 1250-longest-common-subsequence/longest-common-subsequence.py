class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1, text2 = list(text1), list(text2)
        L1, L2 = len(text1), len(text2) 
        
        dp = [[0]*(L2+1) for i in range(L1+1)]

        for i in range(L1):
            for j in range(L2):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j] 
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

        return dp[L1][L2]