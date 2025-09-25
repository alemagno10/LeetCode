class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = [(c, (i+1 < len(p) and p[i+1] == "*")) for i,c in enumerate(p) if c != "*"]

        dp = [[False]*(len(s)+1) for _ in range(len(pattern)+1)]
        dp[0][0] = True

        for i in range(len(pattern)):
            dp[i+1][0] = dp[i][0] if pattern[i][1] else False

        for i, (cp, isStar) in enumerate(pattern):
            for j, cs in enumerate(s):
                if cp == "." or cs == cp:
                    dp[i+1][j+1] = dp[i][j] or (isStar and (dp[i+1][j] or dp[i][j+1]))
                else:
                    dp[i+1][j+1] = False or (isStar and dp[i][j+1])
        
        return dp[len(pattern)][len(s)]