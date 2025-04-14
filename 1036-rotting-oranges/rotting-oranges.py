from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = Deque()
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        fresh = 0
        timestamp = 0

        def isInbound(step):
            return 0 <= step[0] < len(grid) and 0 <= step[1] < len(grid[0]) 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while len(queue) > 0:
            curr = queue.popleft()
            for x,y in moves: 
                step = (curr[0]+x, curr[1]+y)
                if isInbound(step) and grid[step[0]][step[1]] == 1:
                    grid[step[0]][step[1]] = 2
                    queue.append((step[0],step[1],curr[2]+1))
                    timestamp = max(timestamp, curr[2]+1)
                    fresh -= 1
        
        return timestamp if fresh == 0 else -1

        
        