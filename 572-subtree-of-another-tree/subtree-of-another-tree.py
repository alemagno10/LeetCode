# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False

        def sameTree(root, subRoot):
            if root and subRoot:
                left = sameTree(root.left, subRoot.left) 
                right = sameTree(root.right, subRoot.right)
                return root.val == subRoot.val and left and right
            return (root is None) and (subRoot is None)
        
        def findNode(root, subRoot):
            if root:
                if root.val == subRoot.val:
                    self.res |= sameTree(root, subRoot)
                return findNode(root.left, subRoot) or findNode(root.right, subRoot)

        findNode(root, subRoot)
        return self.res