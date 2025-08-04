class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(i):
            if i >= len(s):
                return i == len(s)
            
            key = s[i:len(s)]
            if key in memo:
                return memo[key]
            
            for w in wordDict:
                end = i+len(w)
                if end <= len(s) and s[i:end] == w and dfs(end):
                    memo[key] = True
                    return True

            memo[key] = False
            return False
        
        return dfs(0)
            
