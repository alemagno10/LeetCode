# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left, right = self.dfs(root.left), self.dfs(root.right)

        if left < 0 or right < 0:
            return False
        return abs(self.dfs(root.left) - self.dfs(root.right)) < 2


    def dfs(self, root):
        if not root:
            return 0

        left, right = self.dfs(root.left), self.dfs(root.right)
        if abs(left - right) < 2:
            return 1 + max(left,right)

        return -1000
        