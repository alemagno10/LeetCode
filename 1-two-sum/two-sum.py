class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numbers = {n : idx for idx,n in enumerate(nums)}

        for idx,n in enumerate(nums):
            delta = target - n
            if delta in numbers and numbers[delta] != idx:
                return [idx, numbers[delta]]
        return []
        