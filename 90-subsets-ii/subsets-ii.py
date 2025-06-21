class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, curr = [], []

        def dfs(i):
            if len(nums) <= i:
                print(curr)
                res.append(list(curr))
                return 

            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return res