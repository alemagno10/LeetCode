class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank, start = 0,0
        for location in range(len(gas)):
            tank += gas[location] - cost[location]
            if tank < 0:
                start = location+1
                tank = 0 
        
        return start 
