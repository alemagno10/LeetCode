from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res, l = 0,0
        
        for r,char in enumerate(s):
            while char in window:
                window.remove(s[l])
                l+=1
            window.add(char)
            res = max(res, len(window))
        
        return res
