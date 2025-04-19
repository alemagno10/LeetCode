# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], ts: int) -> int:
        def dfs(node):
            if not node:
                return 0
            return search(node, 0) + dfs(node.left) + dfs(node.right) 
        
        def search(node, v):
            if not node:
                return 0
            v += node.val
            return int(v == ts) + search(node.left,v) + search(node.right,v)
            
        return dfs(root)