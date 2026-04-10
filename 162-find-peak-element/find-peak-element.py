class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        end = len(nums)-1
        l,r = 0, end
        res = 0

        if len(nums) == 1:
            return 0

        while l <= r:
            mid = (l+r)//2
            if mid == end and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                if mid == 0 or nums[mid] > nums[mid-1]:
                    return mid
                r = mid-1

        return res