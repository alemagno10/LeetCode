class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        symbols = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        prev, curr = None, 0
        for i in range(len(s)-1, -1, -1):
            if not prev:
                prev = s[i]
                curr = symbols[s[i]]

            elif symbols[s[i]] == symbols[prev]:
                curr += symbols[s[i]]

            elif symbols[s[i]] > symbols[prev]:
                res += curr
                prev, curr = s[i], symbols[s[i]]

            else:
                curr -= symbols[s[i]]
                res += curr
                prev, curr = None, 0
        
        return res + curr




