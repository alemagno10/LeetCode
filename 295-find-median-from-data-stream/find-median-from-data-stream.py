import heapq

class MedianFinder:
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        self.heap.append(num)
        self.heap.sort()

    def findMedian(self) -> float:
        length = len(self.heap)
        l = math.floor(length/2)
        r = length-l-1
        return (self.heap[l] + self.heap[r])/2        
        