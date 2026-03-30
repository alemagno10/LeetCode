# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target, path):
            if not root:
                return False

            path.append(root)
            if root == target:
                return True

            if dfs(root.left, target, path) or dfs(root.right, target, path):
                return True
            path.pop()
            return False
        
        p1, p2 = [], []
        dfs(root, p, p1)
        dfs(root, q, p2)

        LCA, i = root, 0
        for a,b in zip(p1,p2):
            if a == b:
                LCA = a
        return LCA
