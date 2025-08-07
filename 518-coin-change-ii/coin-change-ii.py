class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
                
        def dfs(amt, i):
            if amt <= 0:
                return int(amt == 0)
            
            if i == len(coins):
                return 0
            
            key = (amt,i)
            if key in memo:
                return memo[key]
            
            res = dfs(amt-coins[i], i) + dfs(amt, i+1)
            
            memo[key] = res
            return res
        
        return dfs(amount,0)
