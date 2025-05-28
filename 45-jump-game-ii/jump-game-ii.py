from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = -1
        queue = deque([0])
        visited = set()

        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr >= len(nums):
                    continue

                for i in range(curr+1, curr+nums[curr]+1):
                    if i not in visited and i < len(nums):
                        queue.append(i)
                        visited.add(i)
            jumps+=1

        return jumps