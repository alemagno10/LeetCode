class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "/", "*", "-"}

        while len(tokens) > 1:
            idx = 0
            while tokens[idx] not in operators:
                idx += 1
            
            op = tokens.pop(idx)
            value2 = tokens.pop((idx-1))
            value1 = tokens.pop((idx-2))

            tokens.insert(idx-2, int(eval(f'{int(value1)} {op} {int(value2)}')))
        
        return int(tokens[0])

