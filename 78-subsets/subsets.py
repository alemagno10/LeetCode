class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(curr, i):
            if i == len(nums):
                res.append(list(curr))
                return
            
            backtracking(curr,i+1)
            curr.append(nums[i])
            backtracking(curr,i+1)
            curr.pop()
        
        backtracking([],0)
        return res
