class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        nums.sort()

        maxGap = 0
        for i in range(len(nums)-1):
            maxGap = max(maxGap, abs(nums[i] - nums[i+1]))
        return maxGap