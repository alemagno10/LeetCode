from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
    
    def longer(self):
        if len(self.small) < len(self.large):
            return self.small, self.large
        return self.large, self.small
        
    def addNum(self, num: int) -> None:
        if len(self.small) == 0 or num > -self.small[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -num)
        if abs(len(self.small)-len(self.large)) > 1:
            a, b = self.longer()
            val = heappop(b)
            heappush(a,-val)
        
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        return (-self.small[0] + self.large[0])/2
