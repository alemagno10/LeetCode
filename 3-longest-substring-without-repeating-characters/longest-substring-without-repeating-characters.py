from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest,curr = 0,0
        seen = set()
        queue = deque()

        for char in s:
            longest = max(longest, curr)
            if char in seen:

                while True:
                    discarted = queue.popleft()
                    seen.remove(discarted)
                    curr-=1
                    if char == discarted:
                        break

            curr += 1
            seen.add(char)
            queue.append(char)

        return max(longest, curr)



        
