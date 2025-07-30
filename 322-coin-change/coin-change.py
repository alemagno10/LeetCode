class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        coins.sort()

        def search(amount):
            if amount in memo:
                return memo[amount]
            
            if amount < coins[0]:
                return float("inf") 

            best = float("inf")           
            for coin in coins:
                if coin <= amount:
                    coins_needed = 0
                    if amount % coin == 0:
                        coins_needed = amount // coin
                    else: 
                        coins_needed = 1+search(amount-coin)
                    best = min(best, coins_needed)

            memo[amount] = best
            return best
        
        minCoins = search(amount)
        return minCoins if minCoins != float("inf") else -1
                
            
                  