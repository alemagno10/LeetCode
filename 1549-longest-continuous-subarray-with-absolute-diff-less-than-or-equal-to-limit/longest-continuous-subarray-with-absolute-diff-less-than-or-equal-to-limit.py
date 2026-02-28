from heapq import heappush, heappop

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lcs, l = 0, 0
        minheap, maxheap = [], [] 
        window = {}

        for r,curr in enumerate(nums):
            heappush(minheap, curr)
            heappush(maxheap, -curr)
            window[curr] = window.get(curr, 0) + 1 

            while l<=r and (abs(curr - minheap[0]) > limit or abs(curr + maxheap[0]) > limit):
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    window.pop(nums[l])

                while minheap[0] not in window:
                    heappop(minheap)
                
                while -maxheap[0] not in window:
                    heappop(maxheap)
                l += 1
            
            lcs = max(lcs, r-l+1)

        return lcs
