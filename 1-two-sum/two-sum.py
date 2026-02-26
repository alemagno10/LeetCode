class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i,n in enumerate(nums):
            pair = target - n
            if pair in index:
                return [index[pair], i]
            index[n] = i 