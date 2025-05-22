class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        if target < candidates[0]:
            return []

        def backtracking(curr,target,i):
            if target < 0 or i >= len(candidates):
                return

            if target == 0:
                res.append(list(curr))
                return 

            n = candidates[i]

            curr.append(n)
            backtracking(curr, target-n, i)
            curr.pop()

            backtracking(curr,target,i+1)

        backtracking([],target,0)
        return res
            
        

            

            