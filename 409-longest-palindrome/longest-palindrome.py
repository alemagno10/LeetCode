class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        res, seenOdd = 0, False
        for v in counter.values():
            if v % 2 == 0:
                res += v
            else:
                res += v - int(seenOdd)
                seenOdd = True
        
        return res


        


