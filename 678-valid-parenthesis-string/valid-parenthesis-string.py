class Solution:
    def checkValidString(self, s: str) -> bool:
        cache = {}

        def dfs(i, left):
            if i == len(s) or left < 0:
                return left == 0
            
            key = (i,left)
            if key not in cache: 
                if s[i] == "(":
                    cache[key] = dfs(i+1, left+1)
                elif s[i] == ")":
                    cache[key] = dfs(i+1, left-1)
                else:
                    cache[key] = dfs(i+1, left+1) or dfs(i+1, left-1) or dfs(i+1, left)
            return cache[key]
        
        return dfs(0,0)