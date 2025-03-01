class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while len(stack) > 0 and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1

        while len(stack) > 0 and stack[0] == "0":
            stack.pop(0)

        res = "".join(stack)
        return str(res) if res else "0"
