class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        pp, p = cost[0], cost[1]

        for cth in cost[2:]:
            pp, p = p, cth+min(pp,p)
        
        return p