class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        singlesXORted = 0

        for n in nums:
            singlesXORted ^= n
        
        #find least significant bit mask
        mask = 1
        for i in range(32):
            if singlesXORted & mask == 0:
                mask <<= 1
            else:
                break
        
        groupA, groupB = 0,0
        for n in nums:
            if n & mask == 0:
                groupA ^= n
            else:
                groupB ^= n
    
        return [groupA, groupB]

          