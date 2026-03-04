"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def same(x,y,size):
            target = grid[x][y]
            for i in range(x, x+size):
                for j in range(y, y+size):
                    if grid[i][j] != target:
                        return False
            return True
        
        def build(x,y,size):
            if same(x,y,size):
                return Node(bool(grid[x][y]), True)

            half = size//2
            quadrant = [(x,y), (x,y+half), (x+half,y), (x+half, y+half)]
            children = [build(m,n,half) for m,n in quadrant]
            node = Node(True, False, *children)
            return node

        return build(0,0,len(grid))