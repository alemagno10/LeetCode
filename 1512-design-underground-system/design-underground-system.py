import numpy as np
from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.times = defaultdict(list)
        self.checkins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
        
    def checkOut(self, id: int, stationB: str, t: int) -> None:
        stationA, timeA = self.checkins[id]
        self.times[stationA, stationB].append(t-timeA)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return np.mean(self.times[startStation,endStation])  
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)