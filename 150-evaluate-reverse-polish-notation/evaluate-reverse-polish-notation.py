class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "/", "*"}
        stack = []

        for token in tokens:
            if token in operators:
                b,a = stack.pop(), stack.pop()
                stack.append(int(eval(f'{a}{token}{b}')))
            else:
                stack.append(token)
        
        return int(stack[-1])