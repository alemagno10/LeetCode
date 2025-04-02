from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longestSubstring = 0,0
        chars = defaultdict(int)

        def isValid(l,r):
            mostfreq = max(chars, key=chars.get) 
            return (1+r-l) - chars[mostfreq] <= k
            
        for r in range(len(s)): 
            chars[s[r]] += 1

            while not isValid(l,r):
                chars[s[l]] -= 1
                l += 1

            longestSubstring = max(longestSubstring, 1+r-l)

        return longestSubstring

