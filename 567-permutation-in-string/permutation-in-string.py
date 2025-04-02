from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = Counter(s1)
        s2_chars = defaultdict(int)
        k = len(s1)

        if len(s1) > len(s2):
            return False

        def isValid():
            for c in s1_chars:
                if s1_chars[c] > s2_chars[c]:
                    return False
            return True

        for i in range(k):
            s2_chars[s2[i]] += 1

        if isValid():
            return True

        for r in range(len(s1), len(s2)):
            s2_chars[s2[r-k]]-=1
            s2_chars[s2[r]]+=1

            if isValid():
                return True
                
        return False
