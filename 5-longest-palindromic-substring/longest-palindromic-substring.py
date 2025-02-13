class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0

        for idx in range(len(s)):
            i,j = idx, idx
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > resLen:
                    res = s[i:j+1]
                    resLen = j - i + 1
                i -= 1
                j += 1
            
            i,j = idx, idx+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > resLen:
                    res = s[i:j+1]
                    resLen = j - i + 1
                i -= 1
                j += 1
        
        return res
