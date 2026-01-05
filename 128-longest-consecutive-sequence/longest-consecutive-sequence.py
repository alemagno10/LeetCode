class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        lcs = 0

        for n in nset:
            seq = 0
            if n-1 in nset:
                continue
            while n+seq in nset:
                seq += 1
            lcs = max(lcs, seq)
        return lcs
            