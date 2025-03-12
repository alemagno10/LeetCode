"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        adjacency = {}
        self.dfs(adjacency, node)

        new_nodes = [Node(i) for i in range(1,len(adjacency)+1)]

        for new in new_nodes:
            new.neighbors += [new_nodes[i-1] for i in adjacency[new.val]]
    
        return new_nodes[0]
    
    def dfs(self, adjacency, node):
        if (not node) or (node in adjacency):
            return 

        adjacency[node.val] = list(map(lambda x: x.val, node.neighbors))
        for adj in node.neighbors:
            if adj.val not in adjacency:
                self.dfs(adjacency, adj)