class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, numSet = list(set(nums)), set(nums)
        visited = dict()
        lcs = 0

        for n in nums:
            if n in visited:
                continue

            seq = 1
            while n+seq in numSet:
                visited[n+seq] = 1
                seq += 1

            visited[n] = seq
            lcs = max(lcs, seq)
        
        return lcs
