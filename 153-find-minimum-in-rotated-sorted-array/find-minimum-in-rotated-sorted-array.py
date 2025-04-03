class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1

        while end > start:
            mid = (start+end)//2
            if nums[start] < nums[mid] < nums[end]:
                return nums[start]
            if  nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[start] > nums[mid]:
                end = mid-1
            else:
                start = mid+1
        
        return nums[start]           
