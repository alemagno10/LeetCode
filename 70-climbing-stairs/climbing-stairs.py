class Solution:
    def climbStairs(self, n: int) -> int:
        pp, p = 0,1

        for i in range(n):
            pp, p = p, p+pp
        
        return p