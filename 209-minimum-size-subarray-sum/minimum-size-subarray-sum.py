class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, window = 0, 0
        length = float('inf')

        for r in range(len(nums)): 
            window += nums[r]
            while window >= target:
                length = min(length, r-l+1)
                window -= nums[l]
                l += 1
        
        return length if length != float('inf') else 0