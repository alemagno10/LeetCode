class Solution:
    def rob(self, houses: List[int]) -> int:
        pp, p = 0, 0

        for house in houses:
            pp, p = p, max(house+pp, p)
        
        return p