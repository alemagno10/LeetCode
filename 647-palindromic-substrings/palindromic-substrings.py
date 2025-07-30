class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for curr in range(len(s)):
            for i in [0,1]:
                l,r = curr, curr+i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    counter += 1
                    l, r = l-1, r+1
            
        return counter