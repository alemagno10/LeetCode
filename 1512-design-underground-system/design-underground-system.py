import numpy as np
from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.times = defaultdict(lambda: (0,0))
        self.checkins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)
        
    def checkOut(self, id: int, stationB: str, t: int) -> None:
        stationA, timeA = self.checkins[id]
        summ, n = self.times[stationA, stationB] 
        self.times[stationA, stationB] = (summ+(t-timeA), n+1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        summ, n = self.times[startStation, endStation]
        return summ/n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)