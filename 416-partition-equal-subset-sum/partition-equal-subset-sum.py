class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo, SUM = dict(), sum(nums)
        if SUM % 2 != 0:
            return False
        
        def dfs(re, i):
            key = (re, i)
            if re <= 0 or len(nums) == i:
                return re == 0
            
            if key in memo:
                return memo[key]
            
            res = dfs(re, i+1) or dfs(re - nums[i], i+1)
            memo[key] = res
            return res
        
        target = SUM/2
        return dfs(target, 0)