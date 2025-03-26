from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        rows = [set() for _ in range(length)]
        cols = [set() for _ in range(length)]
        subbox = defaultdict(set)

        for i in range(length):
            for j in range(length):
                digit = board[i][j]
                if digit == ".":
                    continue
                
                key = (self.imap(i), self.imap(j))
                if (digit in rows[i]) or (digit in cols[j]) or (digit in subbox[key]):
                    return False
                
                rows[i].add(digit)
                cols[j].add(digit)
                subbox[key].add(digit)

        return True

    def imap(self, x):
        if x <= 2:
            return 0
        return 1 if x <= 5 else 2