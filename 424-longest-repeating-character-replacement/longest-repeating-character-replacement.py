from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        l, res = 0,0

        for r,c in enumerate(s):
            counter[c] += 1
            while r-l+1 - max(counter.values()) > k:
                counter[s[l]] -= 1
                l+=1
            res = max(res,r-l+1)
        return res
