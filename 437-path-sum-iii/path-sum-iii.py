# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root):
            if not root:
                return 0

            validPaths = search(root,targetSum)
            return validPaths + dfs(root.left) + dfs(root.right)
        
        def search(root, ts):
            if not root:
                return False
            
            ts -= root.val
            return int(ts == 0) + search(root.left, ts) + search(root.right, ts)
    
        return dfs(root)