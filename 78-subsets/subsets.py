class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(curr,i):   
            if i == len(nums):
                res.append(curr)
                return 
            backtracking(curr+[],i+1), 
            backtracking(curr+[nums[i]],i+1)

        backtracking([],0)
        return res
