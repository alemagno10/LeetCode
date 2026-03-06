from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        queue = deque()
        n, m = len(grid), len(grid[0])

        def outOfbounds(x,y):
            return not(0 <= x < len(grid) and 0 <= y < len(grid[0]))

        def markIsland(x,y):
            if outOfbounds(x,y) or grid[x][y] != 1:
                return 
            grid[x][y] = 2
            queue.append((x,y))
            for dx, dy in moves:
                markIsland(x+dx, y+dy)
            return True
   
        def defineIsland():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] and markIsland(i, j):
                        return
        
        defineIsland()

        visited = set(queue) 
        bridge = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m) or (nx, ny) in visited:
                        continue
                    if grid[nx][ny] == 1:
                        return bridge
                    visited.add((nx, ny))
                    queue.append((nx, ny))
            bridge += 1

        return -1