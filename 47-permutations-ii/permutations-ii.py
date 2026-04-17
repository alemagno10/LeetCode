from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res, n = [], len(nums)

        def dfs(curr):
            if len(curr) == n:
                res.append(list(curr))
                return 
            
            for k,v in counter.items():
                if v == 0:
                    continue
                curr.append(k)
                counter[k] -= 1
                dfs(curr)
                curr.pop()
                counter[k] += 1
        
        dfs([])
        return res