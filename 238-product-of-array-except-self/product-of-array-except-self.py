class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [1]*N
        for i in range(N-1):
            prefix[i+1] = prefix[i] * nums[i]
        
        suffix = [1]*N
        for i in range(N-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        return [a*b for a,b in zip(prefix, suffix)]

        