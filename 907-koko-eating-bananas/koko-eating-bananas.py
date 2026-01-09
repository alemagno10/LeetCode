class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        while l < r:
            mid = (l+r)//2
            hours = sum(map(lambda x: math.ceil(x/mid), piles))
            if hours <= h:
                r = mid
            elif hours > h:
                l = mid+1
            else:
                return mid
        
        return r
        
