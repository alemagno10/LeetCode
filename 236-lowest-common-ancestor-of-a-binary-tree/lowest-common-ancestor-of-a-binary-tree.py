# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = [root]

        def dfs(node):
            if not node:
                return False
            
            isTarget = (node == p) or (node == q)
            left, right = dfs(node.left), dfs(node.right)
            if int(isTarget) + int(left) + int(right) == 2:
                LCA[0] = node

            return isTarget or left or right

        dfs(root)
        return LCA[0]
            

