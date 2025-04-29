class Solution:
    def maxProduct(self, words: List[str]) -> int:
        chars = [set(w) for w in words]
        res = 0

        for i in range(len(chars)):
            for j in range(len(chars)):
                if i == j:
                    continue
                
                valid = True
                for char in chars[i]:
                    if char in chars[j]:
                        valid = False
                if valid:
                    res = max(res, len(words[i])*len(words[j]))

        return res