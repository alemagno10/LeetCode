class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, element = 1, nums[0]

        for i in nums:
            if i == element:
                count += 1
            else:
                count -= 1
            

            if count == 0:
                count, element = 1, i
        
        return element
            
