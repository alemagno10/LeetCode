class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, curr = 0,0

        for n in nums:
            curr = curr+1 if n == 1 else 0
            res = max(res, curr)

        return res