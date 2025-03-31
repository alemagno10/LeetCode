class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:       
        start, end = 1, max(piles)
        res = (start+end)//2
        while start <= end:
            mid = (start+end)//2
            if self.timeToEat(piles, mid, h):
                res, end = mid, mid-1
            else:
                start = mid+1

        return res
    
    def timeToEat(self, piles, k, h):
        hoursNeeded = 0
        for pile in piles:
            hoursNeeded += math.ceil(pile/k)
        return hoursNeeded <= h