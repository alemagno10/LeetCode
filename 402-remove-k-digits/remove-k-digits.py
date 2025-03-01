class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while len(stack) > 0 and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            if stack or (not stack and digit != "0"):
                stack.append(digit)
        
        stack = stack[:len(stack)-k]

        res = "".join(stack)
        return str(res) if res else "0"
