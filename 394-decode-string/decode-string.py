class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                word, times = "", ""
                while stack and stack[-1].isalpha():
                    word = stack.pop() + word
                stack.pop()
                while stack and stack[-1].isdigit():
                    times = stack.pop() + times
                stack.append(word*int(times))
            else:
                stack.append(s[i])
        return "".join(stack)