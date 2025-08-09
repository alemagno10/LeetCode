class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1e9]*len(prices) for i in range(2)]

        def dfs(holding, i):
            if i >= len(prices):
                return 0
            
            if dp[holding][i] > -1e9:
                return dp[holding][i]

            if holding:
                op = dfs(0, i+2) + prices[i]  # sell
            else:
                op = dfs(1, i+1) - prices[i] # buy

            keep = dfs(holding, i+1)
            dp[holding][i] = max(op, keep)
            return dp[holding][i]

        return dfs(0, 0)