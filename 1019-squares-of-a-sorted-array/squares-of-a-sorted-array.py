class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key=lambda x: abs(x))
        return [abs(x)**2 for x in nums]