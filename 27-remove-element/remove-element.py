class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k+=1
                nums[i] = float('inf')
        
        nums.sort()
        return len(nums)-k
