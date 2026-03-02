# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left, right, leaves = [], [], []

        def isBoundary(node):
            return node != root and (bool(node.left) or bool(node.right)) 

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node != root and not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.right)
        
        def dfsL(node):
            if not node:
                return
            if isBoundary(node):
                left.append(node.val)
            if node.left:
                dfsL(node.left) 
            else:
                dfsL(node.right)
    
        def dfsR(node):
            if not node:
                return
            if node.right:
                dfsR(node.right)
            else:
                dfsR(node.left) 
            if isBoundary(node):
                right.append(node.val)
        
        dfs(root)
        dfsL(root.left)
        dfsR(root.right)
        return [root.val] + left + leaves + right