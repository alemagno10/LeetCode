class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        visited = set()
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(pos):
            x,y = pos

            if not(0 <= x < len(board)) or not(0 <= y < len(board[0])):
                return

            visited.add(pos)
            
            if board[x][y] == "X":
                return 
        
            board[x][y] = "K"
            for mov in moves:
                step = (x+mov[0], y+mov[1])
                if step not in visited:
                    dfs(step)
        
        for x in range(len(board)):
            for y in (0, len(board[0])-1):
                dfs((x,y))
        
        for x in (0, len(board)-1):
            for y in range(len(board[0])):
                dfs((x,y))
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                point = board[x][y]
                board[x][y] = "O" if point == "K" else "X" if point == "O" else "X"