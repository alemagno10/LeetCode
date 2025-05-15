# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def search(node, maxV):
            if node is None:
                return 0
            isGood = int(node.val >= maxV)
            maxV = max(maxV, node.val)
            return isGood + search(node.left, maxV) + search(node.right, maxV) 

        return search(root, float('-inf'))
        