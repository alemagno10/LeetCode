class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        def time(pos1, pos0, speed):
            return (pos1 - pos0) / speed

        cars = [(pos[i],speed[i],time(target,pos[i],speed[i])) for i in range(len(pos))]
        cars = sorted(cars, key=lambda x: x[0], reverse=True) 

        fleet = len(pos)
        for i in range(1,len(pos)):
            prev,curr = cars[i-1], cars[i] 
            if prev[2] == curr[2]:
                fleet -= 1
            elif prev[2] > curr[2]:
                fleet -= 1
                cars[i] = (curr[0],curr[1],prev[2])

        return fleet   