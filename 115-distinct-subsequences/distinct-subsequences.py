class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        dp = [[0]*(len(s)+1) for i in range(len(t))]
        dp.insert(0,[1]*(len(s)+1))

        for i in range(len(t)):
            for j in range(len(s)):
                dp[i+1][j+1] = dp[i+1][j] 
                if t[i] == s[j]:  
                    dp[i+1][j+1] += dp[i][j] 

        return dp[len(t)][len(s)]

