class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        res,l,r = 0,0,len(arr)-1

        while l <= r:
            mid = (l+r)//2
            if mid >= 1 and arr[mid-1] > arr[mid]:
                r = mid-1
            else:
                if arr[mid] > arr[res]:
                    res = mid
                l = mid+1
        
        return res

