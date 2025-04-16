from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queenPos = {i:-1 for i in range(n)}
        colsUsed = set()
        dots = ["."]*n
        res = []

        def noDiagonals(row,col):
            for i in (-1,1):
                step = (row,col)
                while 0 <= step[0] < n and 0 <= step[1] < n:
                    if queenPos[step[0]] == step[1]:
                        return False
                    step = (step[0]-1,step[1]+i)
            return True
        
        def replaceByIndex(lst, i, val):
            lst[i] = val
            return lst

        def backtracking(row):
            if row == n:
                res.append(["".join(replaceByIndex(deepcopy(dots), q, "Q")) for q in queenPos.values()])
            
            for col in range(n):
                if col not in colsUsed and noDiagonals(row,col):
                    lastCol, queenPos[row] = queenPos[row], col
                    colsUsed.add(col)
                    backtracking(row+1)
                    queenPos[row] = lastCol
                    colsUsed.remove(col)
        
        backtracking(0)
        return res