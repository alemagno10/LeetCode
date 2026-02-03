class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, curr = 0,0
        res = float('-inf')

        for r in range(len(nums)):
            if curr < 0:
                curr = 0
            curr += nums[r]
            res = max(res, curr)
        return res