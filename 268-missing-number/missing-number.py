class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            res = sum(range(len(nums)+1))
            nums = sum(nums)
            return res-nums
