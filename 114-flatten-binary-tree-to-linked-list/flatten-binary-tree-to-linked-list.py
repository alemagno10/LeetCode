# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        aux = []
        if not root:
            return None

        def search(node):
            if not node:
                return None

            aux.append(node)
            left = search(node.left)
            right = search(node.right)
            node.left, node.right = None, None
        
        search(root)
        head = aux.pop(0)
        node = head
        for curr in aux:
            node.right = curr
            node = node.right
        
        return head

