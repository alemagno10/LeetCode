class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = defaultdict(int)

        for c in s:
            letters[c] += 1

        res, seenOdd = 0, False
        for k,v in letters.items():
            if v % 2 == 0:
                res += v
            else:
                res += v - int(seenOdd)
                seenOdd = True
        
        return res


        


