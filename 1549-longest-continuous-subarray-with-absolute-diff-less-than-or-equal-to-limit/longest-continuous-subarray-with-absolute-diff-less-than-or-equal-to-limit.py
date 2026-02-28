from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lcs, l = 0, 0
        minQ, maxQ = deque(), deque() 

        for r,curr in enumerate(nums):
            while minQ and curr < minQ[-1]:
                minQ.pop()
            minQ.append(curr)

            while maxQ and curr > maxQ[-1]:
                maxQ.pop()
            maxQ.append(curr)

            while maxQ and minQ and (maxQ[0] - minQ[0] > limit):
                if minQ and minQ[0] == nums[l]:
                    minQ.popleft()
                if maxQ and maxQ[0] == nums[l]:
                    maxQ.popleft()
                l += 1

            lcs = max(lcs, r-l+1)

        return lcs
