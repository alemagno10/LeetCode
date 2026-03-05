class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = 1e4

        while l <= r:
            mid = (l+r)//2
            L, R, MID = nums[l], nums[r], nums[mid]

            if L > R:
                if L < MID:
                    l = mid+1
                else:
                    res = min(res, MID, R)
                    r = mid-1
            else:
                res = min(res, L)
                return res
        
        return res