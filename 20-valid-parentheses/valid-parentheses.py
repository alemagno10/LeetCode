class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pars = {"}":"{" ,"]":"["  ,")":"("}
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
            elif char == "}" or char == "]" or char == ")":
                if not stack or pars[char] != stack.pop():
                    return False
        return len(stack) == 0