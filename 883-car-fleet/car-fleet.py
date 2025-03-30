class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = lambda p,s: (target - p)/s
        cars = sorted(((p,s,time(p,s)) for p,s in zip(position, speed)), key=lambda x: -x[0])
        fleets = len(position)
        currtime = cars[0][2]

        for i in range(1,len(cars)):
            if cars[i][2] <= currtime:
                fleets -= 1
            else:
                currtime = cars[i][2]


        return fleets




# target = 12, 
# position = [10,8,0,5,3]
# speed =    [2,4,1,1,3]
# time =     [1,1,12,7,3]

# fleet = 3
# currT <= lastT

# 10,8,0,5,3

# 0,,,3,,5,,,8,,10

# s = so + vt
# 12 = 10 + 2*t

# 2/2 = t
# t = 1

# stack = [
#    7
# ]