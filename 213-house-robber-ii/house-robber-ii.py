class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        rob_first = self.robHouses(nums[:-1])
        rob_last = self.robHouses(nums[1:])
        return max(rob_first, rob_last)

    def robHouses(self, nums: List[int]) -> int:
        pp, p = 0,0
        for i in nums:
            pp, p = p, max(pp+i,p)
        return p