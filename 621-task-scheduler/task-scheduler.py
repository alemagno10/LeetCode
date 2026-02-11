from heapq import heapify, heappop, heappush
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []

        for v in counter.values():
            heappush(heap, [0,-v])

        time = 0
        while heap:
            if heap[0][0] <= time: 
                task = heappop(heap)
                task[0], task[1] = task[0]+n+1, task[1]+1
                if task[1] < 0:
                    heappush(heap, task)
            time += 1

        return time
