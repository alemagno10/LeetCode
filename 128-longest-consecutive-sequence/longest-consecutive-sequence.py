class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        visited = set()
        longest_seq = 0

        for curr in nums:
            if curr in visited:
                continue

            seq = 1
            less, greater = curr-1, curr+1
            while less in nums:
                seq+=1
                visited.add(less)
                less-=1

            while greater in nums:
                seq+=1
                visited.add(greater)
                greater+=1
            
            longest_seq = max(seq, longest_seq)
        
        return longest_seq
