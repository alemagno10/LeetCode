class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = (-1,10**5)
        window, t_chars = defaultdict(int), defaultdict(int)
        notGood = set()

        for char in t:
            t_chars[char] += 1
            notGood.add(char)
        
        l = 0
        for r,char in enumerate(s):
            if char in t_chars:
                window[char] += 1
                if char in notGood and window[char] >= t_chars[char]:
                    notGood.remove(char)

            while len(notGood) == 0 and l<=r:
                if r-l < res[1] - res[0]:
                    res = (l,r)
                
                if s[l] in t_chars:
                    window[s[l]] -= 1
                    if window[s[l]] < t_chars[s[l]]:
                        notGood.add(s[l])
                l += 1
        
        return s[res[0]:res[1]+1] if res[0] > -1 else ""
