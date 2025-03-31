class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0, len(nums)-1

        while end >= start:
            mid = math.floor((end+start)/2)
            if target < nums[mid]:
                end = mid-1
            elif target > nums[mid]:
                start = mid+1
            else:
                return mid

        return -1