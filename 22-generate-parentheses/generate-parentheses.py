class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtracking(op,cl):
            if op == 0 and cl == 0:
                res.append("".join(curr))
                return 
            if op > 0:
                curr.append("(")
                backtracking(op-1,cl)
                curr.pop()
            if cl > 0 and cl > op:
                curr.append(")")
                backtracking(op,cl-1)
                curr.pop()
        
        backtracking(n,n)
        return res


