class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        LCP = 0
        minWord = min(strs, key=lambda x: len(x))
        
        for i in range(len(minWord)):
            char = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != char:
                    return strs[0][:LCP]
            LCP += 1
        return strs[0][:LCP]
