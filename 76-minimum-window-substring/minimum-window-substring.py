class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = ""
        window, t_chars = defaultdict(int), defaultdict(int)

        def isValid():
            for c in t_chars:
                if t_chars[c] > window[c]:
                    return False
            return True

        for char in t:
            t_chars[char] += 1
        
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            while isValid():
                if res == "" or 1+r-l < len(res):
                    res = s[l:r+1]
                window[s[l]] -= 1
                l += 1
        
        return res