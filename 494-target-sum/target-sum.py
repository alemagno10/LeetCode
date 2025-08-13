from collections import defaultdict
from copy import deepcopy

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        SUM = sum(nums)
        dp = [defaultdict(int) for i in range(len(nums)+1)]

        dp[0][0] = 1
        for i in range(len(nums)):
            for k,v in dp[i].items():
                dp[i+1][k+nums[i]] += v 
                dp[i+1][k-nums[i]] += v 

        return dp[len(nums)][target]