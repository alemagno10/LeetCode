class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        mapper, used = dict(), set()

        if len(words) != len(pattern):
            return False

        for i,word in enumerate(words):
            if word not in mapper:
                if pattern[i] in used:
                    return False
                mapper[word] = pattern[i]
                used.add(pattern[i])
            elif mapper[word] != pattern[i]:
                return False
        return True
            