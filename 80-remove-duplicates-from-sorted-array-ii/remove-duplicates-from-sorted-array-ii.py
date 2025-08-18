class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, count = nums[0], 1
        k,l = 0,0

        for r in range(1,len(nums)):
            if nums[r] == curr:
                count += 1
            else:
                curr, count = nums[r], 1
            
            if count > 2:
                nums[r] = 1e9
                k += 1

            while l < r and nums[l] != 1e9:
                l += 1
            
            if nums[l] == 1e9:
                nums[l], nums[r] = nums[r], 1e9
            
        return len(nums)-k


