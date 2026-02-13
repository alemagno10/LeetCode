class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1,x
        res = 0

        while l<=r:
            mid = (r+l)//2 
            if mid**2 < x:
                l = mid+1
                res = mid
            elif mid**2 > x:
                r = mid-1
            else:
                return mid
        return res