class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}
        for digit in nums:
            counter[digit] = counter.get(digit, 0) + 1
        
        for freq in counter.values():
            if freq % 2 != 0:
                return False
        
        return True