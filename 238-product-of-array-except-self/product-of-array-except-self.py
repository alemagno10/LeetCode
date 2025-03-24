class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        pos = [1]*len(nums)

        for i in range(1,len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        for i in range(len(nums)-2,-1,-1):
            pos[i] = pos[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            nums[i] = pre[i]*pos[i]
        
        return nums