class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTracking(curr, remaining):
            if len(remaining) == 0:
                res.append(list(curr))
                return
            
            for j in list(remaining):
                curr.append(j)
                remaining.remove(j)
                backTracking(curr, remaining)
                curr.pop()
                remaining.add(j)
        
        backTracking([],set(nums))
        return res