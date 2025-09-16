class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if len(haystack) - i < len(needle):
                break

            j = 0
            while j < len(needle) and haystack[i+j] == needle[j]:
                if j == len(needle) - 1:
                    return i
                j += 1 
            
        return -1