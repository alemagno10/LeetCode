# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, wanted) -> List[TreeNode]:
            if wanted.val == root.val:
                return [root]

            if wanted.val > root.val:
                ancestors = dfs(root.right, wanted)
            elif wanted.val < root.val:
                ancestors = dfs(root.left, wanted)

            ancestors.append(root)
            return ancestors

        ancA = dfs(root,p)
        ancB = set(dfs(root,q))

        for v in ancA:
            if v in ancB:
                return v
        return root
