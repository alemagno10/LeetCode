class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [1e9]*(amount+1)
        dp[0] = 0
        coins = [c for c in coins if c <= amount]
        
        for coin in coins:
            dp[coin] = 1

        for i in range(1,amount+1):
            for coin in coins:
                if coin < i:
                    dp[i] = min(dp[i], 1+dp[i-coin])

        return dp[amount] if dp[amount] != 1e9 else -1