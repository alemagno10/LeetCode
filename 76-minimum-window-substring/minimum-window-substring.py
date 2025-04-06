class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = (-1,10**5)
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
                if r-l < res[1] - res[0]:
                    res = (l,r)
                window[s[l]] -= 1
                l += 1
        
        print(res)
        return s[res[0]:res[1]+1] if res[0] > -1 else ""
