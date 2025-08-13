class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, SUM):
            if len(nums) == i:
                return SUM == target
            
            key = (i,SUM)
            if key in memo:
                return memo[key]

            ways = dfs(i+1, SUM + nums[i])
            ways += dfs(i+1, SUM - nums[i])
            memo[key] = ways
            return ways

        return dfs(0,0)
            