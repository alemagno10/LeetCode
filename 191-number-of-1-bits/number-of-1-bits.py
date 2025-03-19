import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        mask,setBits = 1,0

        for i in range(ceil(sqrt(n))+1):
            setBits += int((n & mask) != 0)
            mask <<= 1
        
        return setBits