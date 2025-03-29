class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda x,y: x+y, 
            "-": lambda x,y: x-y, 
            "*": lambda x,y: x*y,
            "/": lambda x,y: int(x/y), 
        }

        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                b,a = stack.pop(), stack.pop()
                stack.append(operators[token](a,b))
        
        return int(stack[-1])