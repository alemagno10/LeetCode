class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)
        if SUM % 2 != 0:
            return False
        
        target = SUM/2
        dp = set()

        for n in nums:
            if n == target:
                return True

            new_sums = set()
            for curr_sum in dp:
                curr_sum += n
                if curr_sum == target:
                    return True
                if curr_sum < target:
                    new_sums.add(curr_sum)
            dp.add(n)
            dp.update(new_sums)
            
        return False 