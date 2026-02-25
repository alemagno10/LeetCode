# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root, k):
            if root is None:
                return k
            k = dfs(root.left, k) - 1
            if k == 0:
                res.append(root.val)
            return dfs(root.right, k)
        
        dfs(root, k)
        return res[0]