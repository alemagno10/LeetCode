class Solution:
    def numDecodings(self, s: str) -> int:
        pp, p = 0, 1

        for i in range(len(s)):
            ways = 0

            if s[i] != "0":
                ways += p
            if i > 0 and (s[i-1] == "1" or (s[i-1] == "2" and s[i] < "7")):
                ways += pp

            pp, p = p, ways
        
        return p