class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while end > start:
            mid = (start+end)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if nums[end] >= target > nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
                    
        return start if nums[start] == target else -1

        
