class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(curr,op,cl):
            if op == 0 and cl == 0:
                res.append(curr)
                return 
            if op > 0:
                dfs(curr+"(",op-1,cl)
            if cl > 0 and cl > op:
                dfs(curr+")",op,cl-1)
        
        dfs("",n,n)
        return res
