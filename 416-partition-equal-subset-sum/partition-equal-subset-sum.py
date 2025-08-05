class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        memo = {}
        def dfs(subset, i):
            s1, s2 = subset
            key = (subset,i)

            if i == len(nums):
                return s1 == s2
            
            if key in memo:
                return memo[key]
            
            res = dfs((s1+nums[i], s2), i+1) or dfs((s1, s2+nums[i]), i+1)
            memo[key] = res
            return res
        
        return dfs((0,0),0) 