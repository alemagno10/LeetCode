class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, visited = set(nums), set()
        lcs = 0

        for n in nums:
            if n in visited or n-1 in nums:
                continue

            seq = 0
            while n+seq in nums:
                visited.add(n+seq)
                seq += 1

            lcs = max(lcs, seq)
        
        return lcs
