class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def isPalindrome(s):
            return s == s[::-1]

        def dfs(i):
            if i >= len(s):
                res.append(list(part)) 
            for j in range(i+1, len(s)+1):
                partition = s[i:j]
                if isPalindrome(partition):
                    part.append(partition)
                    dfs(j)
                    part.pop()

        dfs(0)
        return res
