

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixCount = {0: 1}
        res,summ = 0,0

        for n in nums:
            summ += n
            diff = summ - k
            res += prefixCount.get(diff,0)
            prefixCount[summ] = prefixCount.get(summ,0) + 1
        
        return res