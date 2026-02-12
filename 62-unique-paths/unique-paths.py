class Solution:
    def uniquePaths(self, ROWS: int, COLS: int) -> int:
        dp = [[1]*COLS for _ in range(ROWS)]

        for m in range(1,ROWS):
            for n in range(1,COLS):
                dp[m][n] = dp[m-1][n] + dp[m][n-1]

        return dp[ROWS-1][COLS-1]