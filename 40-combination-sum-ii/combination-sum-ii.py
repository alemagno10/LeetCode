class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, curr = [], []

        def backtracking(i,amount):
            if amount == target:
                res.append(list(curr))
                return 
            if i >= len(candidates) or amount > target:
                return 
            
            curr.append(candidates[i])
            backtracking(i+1,amount+candidates[i])
            curr.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtracking(i+1,amount)

        backtracking(0,0)
        return res
