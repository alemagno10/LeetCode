from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap, res = [], 0

        for inter in intervals:
            while heap and heap[0] <= inter[0]:
                heappop(heap)
            heappush(heap,inter[1])
            res = max(res, len(heap))
        return res