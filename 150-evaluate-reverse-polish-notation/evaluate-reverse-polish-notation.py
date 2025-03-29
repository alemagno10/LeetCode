class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}

        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                b,a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))
        
        return int(stack[-1])