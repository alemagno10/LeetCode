from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-n for n in Counter(tasks).values()]
        queue = deque()

        heapq.heapify(heap)
        time = 0

        if n == 0:
            return len(tasks)
        
        while(heap or queue):
            if heap:
                task = heapq.heappop(heap)+1
                if task != 0:
                    queue.append((task,time+n))

            while queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
            time+=1

        return time