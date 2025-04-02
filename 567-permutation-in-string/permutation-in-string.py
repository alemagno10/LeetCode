from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars, s2_chars = defaultdict(int), defaultdict(int)

        if len(s1) > len(s2):
            return False

        def isValid():
            for c in s1_chars:
                if s1_chars[c] > s2_chars[c]:
                    return False
            return True

        k = len(s1)
        for i in range(k):
            s1_chars[s1[i]] += 1
            s2_chars[s2[i]] += 1

        for r in range(len(s1), len(s2)):
            if isValid():
                return True

            s2_chars[s2[r-k]]-=1
            s2_chars[s2[r]]+=1
                
        return isValid()
