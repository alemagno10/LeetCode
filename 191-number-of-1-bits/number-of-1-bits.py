import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask,setBits = 1,0

        while n > 0:
            setBits += n & mask
            n >>= 1
        
        return setBits