# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            tree.append(root)
            dfs(root.right)
        
        tree = []
        dfs(root)

        toSwap = None
        for node1, node2 in zip(tree, sorted(tree, key= lambda x: x.val)):
            if node1 == node2:
                continue
            if not toSwap:
                toSwap = node1
            else:
                toSwap.val, node1.val = node1.val, toSwap.val 
        