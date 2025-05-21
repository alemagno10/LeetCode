# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([(root,0)])
        res = [[]]
        depth = 0

        while len(queue) > 0:
            node, level = queue.popleft()

            if level > depth:
                res.append([])
                depth += 1
            
            res[-1].append(node.val)
        
            if node.left: queue.append((node.left, depth+1))
            if node.right: queue.append((node.right, depth+1))
        
        return res





