from collections import Counter
from heapq import heapify, heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)

        heap = [(-v,k) for k,v in counter.items()]
        heapify(heap)

        res = ""
        while heap:
            v,k = heappop(heap)
            if len(res) > 0 and k == res[-1]:
                if len(heap) > 0:
                    v1,k1 = heappop(heap)
                    res += k1
                    if v1 < -1:
                        heappush(heap, (v1+1,k1))
                    heappush(heap, (v,k))
                else:
                    return ""
            else:
                res += k
                if v < -1:
                    heappush(heap, (v+1,k))
        return res






