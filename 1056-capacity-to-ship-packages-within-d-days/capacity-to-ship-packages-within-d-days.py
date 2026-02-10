class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap: int) -> int:
            currVal, currDays = 0,1
            for w in weights:     
                if currVal + w <= cap: 
                    currVal += w
                else:
                    currDays += 1
                    currVal = w
            return currDays <= days

        l,r = max(weights), sum(weights)
        res = r
        while l <= r:
            cap = (l+r)//2 
            if canShip(cap):
                res = min(res,cap)
                r = cap-1
            else:
                l = cap+1
        
        return res